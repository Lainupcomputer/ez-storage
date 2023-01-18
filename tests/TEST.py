from src.ez_storage.ez_storage import Ez_Storage
import logging

# logger
logger = logging.getLogger()
logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG, filemode="w")

test_add = True
test_get = True
test_restore = False
default = Ez_Storage()
if test_add:
    logger.debug("starting: test_add")
    new_array = {"source": 1, "destination": 2}
    new_list = [1, 2]
    override = False
    default.add_storage(mode="o", obj="TEST_o", data="test_daten", value="value", override=override)
    default.add_storage(mode="a", obj="TEST_a", array_data=new_array, override=override)
    default.add_storage(mode="l", obj="TEST_l", data=new_list, override=override)

if test_get:
    logger.debug("starting: test_get")
    logger.debug("result 'o' :" + str(default.get_storage(mode="o", obj="TEST_o", data="test_daten")))
    logger.debug("result 'a' :" + str(default.get_storage(mode="a", obj="TEST_a")))
    logger.debug("result 'l' :" + str(default.get_storage(mode="l", obj="TEST_l")))

if test_restore:
    logger.debug("starting: test_restore")
    # restore with base settings
    default_b = Ez_Storage("b")
    default_b.restore_storage(source="b")
    # restore with internal_config in object mode
    default_io = Ez_Storage("io")
    default_io.internal_config = [("test", "io"), ("object", "object")]
    default_io.restore_storage(source="i", destination="Test_IO", mode="o")
    # restore with internal_config in array mode
    default_ia = Ez_Storage("ia")
    new_array = {"source": 1, "destination": 2}
    default_ia.internal_config = new_array
    default_ia.restore_storage(source="i", destination="Test_IA", mode="a")
    # restore with internal_config in list mode
    default_il = Ez_Storage("il")
    default_il.internal_config = [1, 2]
    default_il.restore_storage(source="i", destination="Test_IL", mode="l")

