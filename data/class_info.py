import inspect
import os.path


class ClassInfo:

    @staticmethod
    def get_dir(clazz):
        return os.path.dirname(
            inspect.getmodule(clazz).__file__)

    @staticmethod
    def _get_args_as_str(*argv):
        list_arg = ""
        for i_arg in argv:
            if len(list_arg) > 0:
                list_arg += ", "
            list_arg += str(i_arg)
        return list_arg

    @staticmethod
    def get_method_properties(clazz, method_name):
        return inspect.signature(clazz.__dict__[method_name])

    @staticmethod
    def get_list_methods(clazz):
        return [func for func in dir(clazz)
                if callable(getattr(clazz, func))
                and not func.startswith("__")]
