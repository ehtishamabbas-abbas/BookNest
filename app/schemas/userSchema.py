from pydantic import BaseModel, EmailStr, field_validator, Field

class CreateUserSchema(BaseModel):
    name: str = Field(...,
        description="The user's name.",
        example="John Doe",
    )
    email: EmailStr  
    password: str = Field(...,
        description="The user's password.",
        example="password",
    )
    role: str 

    @field_validator("name")
    def validate_name(cls, value):
        if value == "" or value is None:
            raise ValueError("Please provide the name")
        return value

    @field_validator("password")
    def validate_password(cls, value):
        if value == "" or value is None:
            raise ValueError("Please provide the password")
        return value