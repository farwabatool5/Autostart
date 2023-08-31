class AccessDeniedException(Exception):
    pass


class AlreadyExistsException(Exception):
    pass


class EmailExistsException(Exception):
    pass


class PhoneExistsException(Exception):
    pass


class UsernameExistsException(Exception):

    pass


class ValidationException(Exception):
    pass


class NotFoundException(Exception):
    pass


class ExternalServiceFailed(Exception):
    pass


class IncorrectParameterFormat(Exception):
    pass


class UnscheduledTask(Exception):
    pass


class MissingValueException(Exception):
    pass


class ConcurrencyException(Exception):
    pass


class UserAlreadyExistsWithSameEmailException(Exception):
    pass


class UserAlreadyExistsWithSamePhoneException(Exception):
    pass


class UserAlreadyExistsWithSameUsernameException(Exception):

    pass


class BookingSlotAlreadyBookedException(Exception):
    pass


class MissingEncryptionKeyException(Exception):
    pass
