from pydantic import BaseModel, Field, EmailStr, SecretStr, validator


class UserRegister(BaseModel):
    email: EmailStr = Field(
        ...,
        title="Email Address",
        description="Valid email address for user registration.",
        example="user@example.com",
    )
    password: SecretStr = Field(
        ...,
        title="Password",
        description="Password must be between 8 and 16 characters long, and contain at least one digit, one letter, and one symbol (e.g., !@#$%). This field is sensitive and should be kept secret.",
        example="StrongPass123!",
    )
    is_superuser: bool = Field(
        False,
        title="Superuser Status",
        description="Set to True if the user is a superuser, otherwise False.",
    )

    @validator("password")
    def validate_password(cls, value):
        # Check for the size of password
        if not (8 <= len(value) <= 16):
            raise ValueError("Password length must be between 8 and 16 characters.")

        # Check for at least one uppercase letter
        if not any(c.isupper() for c in value.get_secret_value()):
            raise ValueError("Password must contain at least one uppercase letter")

        # Check for at least one lowercase letter
        if not any(c.islower() for c in value.get_secret_value()):
            raise ValueError("Password must contain at least one lowercase letter")

        # Check for at least one digit
        if not any(c.isdigit() for c in value.get_secret_value()):
            raise ValueError("Password must contain at least one digit")

        # Check for at least one symbol
        if not any(
            c in "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|" for c in value.get_secret_value()
        ):
            raise ValueError("Password must contain at least one symbol")

        return value


class UserLogin(BaseModel):
    email: EmailStr
    password: SecretStr
