import functools
import inspect
import logging


logger = logging.getLogger("security")


class PermissionDeniedError(Exception):
    pass


def rbac(required_role: str, user_arg_name: str = 'user'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            try:
                bound_args = sig.bind(*args, **kwargs)
            except TypeError as e:
                # This handles cases where the function was called with wrong args
                raise e

            if user_arg_name not in bound_args.arguments:
                raise ValueError(f"RBAC Error: Function '{func.__name__}' expects argument '{user_arg_name}'")

            current_user = bound_args.arguments[user_arg_name]

            user_role = getattr(current_user, 'role', None)

            if user_role != required_role:
                logger.warning(
                    f"Access Denied: User {getattr(current_user, 'id', 'unknown')} "
                    f"with role '{user_role}' tried to access '{func.__name__}'"
                )
                raise PermissionDeniedError(f"User requires role '{required_role}'")

            return func(*args, **kwargs)

        return wrapper

    return decorator


# --- Usage Example ---

from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    role: str


@rbac(required_role='admin')
def delete_database(user: User, db_name: str):
    print(f"Database {db_name} deleted by {user.username}")


@rbac(required_role='admin')
def sensitive_report(report_type, user: User = None):
    print(f"Report {report_type} generated for {user.username}")


admin = User(id=1, username="alice", role="admin")
guest = User(id=2, username="bob", role="guest")


try:
    delete_database(admin, "ProductionDB")

    sensitive_report("Financial", user=admin)

    delete_database(guest, "ProductionDB")

except PermissionDeniedError as e:
    print(f"Caught expected error: {e}")