from slot_booking_backend.general.utils.collections import deep_update
from slot_booking_backend.general.utils.settings import get_setting_from_environment


deep_update(globals(), get_setting_from_environment(ENVVAR_SETTING_PREFIX))  # type: ignore
