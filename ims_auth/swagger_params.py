from drf_yasg import openapi


login_page_params = [
    openapi.Parameter(
        "email", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "password",
        openapi.IN_QUERY,
        format="password",
        required=True,
        type=openapi.TYPE_STRING,
    ),
]


change_password_params = [
    openapi.Parameter(
        "old_password",
        openapi.IN_QUERY,
        format="password",
        required=True,
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "new_password",
        openapi.IN_QUERY,
        format="password",
        required=True,
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "retype_password",
        openapi.IN_QUERY,
        format="password",
        required=True,
        type=openapi.TYPE_STRING,
    ),
]


signup_page_params = [
    openapi.Parameter(
        "first_name", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING),
    openapi.Parameter(
        "email", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING),
    openapi.Parameter(
        "password",
        openapi.IN_QUERY,
        format="password",
        required=True,
        type=openapi.TYPE_STRING,),

]

forgot_password_params = [
    openapi.Parameter(
        "email", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING
    ),
]

reset_password_params = [
    openapi.Parameter(
        "new_password1", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "new_password2", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING
    ),
]

user_create_params = [
    openapi.Parameter("first_name", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("last_name", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("role", openapi.IN_QUERY, type=openapi.TYPE_STRING, enum=["ADMIN", "USER"]),
    openapi.Parameter("email", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("alternate_email", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("profile_pic", openapi.IN_QUERY, type=openapi.TYPE_FILE),
    openapi.Parameter("phone", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("alternate_phone", openapi.IN_QUERY, type=openapi.TYPE_STRING),

    openapi.Parameter("addresses", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING),
    openapi.Parameter("street", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("city", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("state", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("pincode", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("country", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("status", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("is_organization_admin", openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN),
]

user_delete_params = [
    openapi.Parameter(
        "user_id", openapi.IN_QUERY, required=True, type=openapi.TYPE_NUMBER
    ),
]

user_list_params = [
    openapi.Parameter("username", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("email", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter(
        "role", openapi.IN_QUERY, type=openapi.TYPE_STRING, enum=["ADMIN", "USER"]
    ),
    openapi.Parameter(
        "status",openapi.IN_QUERY, type=openapi.TYPE_STRING, enum=["Active", "In Active"],
    ),
]

users_status_params = [
    openapi.Parameter(
        "status",openapi.IN_QUERY, type=openapi.TYPE_STRING,enum=["Active", "Inactive"],
    ),
]

users_delete_params = [
    openapi.Parameter("users_list",openapi.IN_QUERY,type=openapi.TYPE_STRING,
    ),
]

user_update_params = [
    openapi.Parameter("first_name", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("last_name", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("role", openapi.IN_QUERY, type=openapi.TYPE_STRING, enum=["ADMIN", "USER"]),
    openapi.Parameter("email", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("alternate_email", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("phone", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("alternate_phone", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("profile_pic", openapi.IN_QUERY, type=openapi.TYPE_FILE),
    openapi.Parameter("addresses", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING),
    openapi.Parameter("street", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("city", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("state", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("pincode", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("country", openapi.IN_QUERY, type=openapi.TYPE_STRING),
]

