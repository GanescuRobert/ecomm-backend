from pydantic import ConfigDict, BaseModel, EmailStr, SecretStr, field_validator


def get_properties_password_description():
    password_requirements = [
        "between 8 and 16 characters long",
        "contain at least one digit",
        "one uppercase letter",
        "one symbol.",
    ]

    return "Password must be" + ", ".join(password_requirements)


class UserRegister(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "user@example.com",
                "password": "StrongPass123!",
                "is_superuser": False,
            },
            "properties": {
                "email": {
                    "type": "string",
                    "format": "email",
                    "description": "Valid email address for user registration.",
                },
                "password": {
                    "type": "string",
                    "format": "password",
                    "minLength": 8,
                    "maxLength": 16,
                    "description": get_properties_password_description(),
                },
                "is_superuser": {
                    "type": "boolean",
                    "description": "True if the user is a superuser, otherwise False.",
                },
            },
        },
        validate_default=True,
    )

    email: EmailStr
    password: SecretStr
    is_superuser: bool

    @field_validator("password")
    def validate_password(cls, value):
        # Check for the size of password
        if not (8 <= len(value) <= 16):
            raise ValueError("Password length must be between 8 and 16 characters.")

        # Check for at least one uppercase letter
        if not any(c.isupper() for c in value):
            raise ValueError("Password must contain at least one uppercase letter")

        # Check for at least one lowercase letter
        if not any(c.islower() for c in value):
            raise ValueError("Password must contain at least one lowercase letter")

        # Check for at least one digit
        if not any(c.isdigit() for c in value):
            raise ValueError("Password must contain at least one digit")

        # Check for at least one symbol
        if not any(c in "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|" for c in value):
            raise ValueError("Password must contain at least one symbol")

        return value


class UserLogin(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "user@example.com",
                "password": "StrongPass123!",
            },
            "properties": {
                "email": {
                    "type": "string",
                    "format": "email",
                    "title": "Email Address",
                    "description": "Valid email address for user login.",
                    "example": "user@example.com",
                },
                "password": {
                    "type": "string",
                    "format": "password",
                    "title": "Password",
                    "description": "User password for login.",
                    "example": "StrongPass123!",
                },
            },
        },
        validate_default=True,
    )

    email: EmailStr
    password: SecretStr
