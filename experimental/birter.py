class Parameter(object):
    def __init__(self, parameters=None):
        if parameters is None:
            self._parameters = {
                "name": None
            }
        elif type(parameters) is not dict or parameters == {}:
            raise TypeError("ParameterTypeError")
        else:
            for key, value in parameters.items():
                if type(key) is not str or type(value) is not str:
                    raise TypeError("ParameterTypeError")
            self._parameters = parameters

    def addAttr(self, name, value=None):
        if value is None:
            self._parameters.update({str(name): None})
        else:
            self._parameters.update({str(name): str(value)})

    def getAttr(self, name):
        if name in self._parameters.keys():
            return self._parameters[name]
        else:
            raise KeyError("No attribute with named as", name)

    def delAttr(self, name):
        if name in self._parameters.keys():
            del self._parameters[name]
        else:
            raise KeyError("No attribute for deleting in parameters list named as", name)

    def updateAttr(self, name, value):
        if name in self._parameters.keys():
            self._parameters.update({name: value})
        else:
            raise KeyError("No attribute for updating in parameters list named as", name)


class CascadeParameter(Parameter):
    def __init__(self, parameters=None):
        if parameters is None:
            super().__init__(parameters)
            self._parameters.update({
                "description": None,
                "type": None,
                "format": None,
                "required": None,
                "hidden": None
            })
        elif type(parameters) is not dict or parameters == {}:
            raise TypeError("ParameterTypeError")
        else:
            for key, value in parameters.items():
                if type(key) is not str or type(value) is not str:
                    raise TypeError("ParameterTypeError")
            self._parameters = parameters


class GroupParameter(Parameter):
    def __init__(self, parameters=None):
        if parameters is None:
            super().__init__(parameters)
            self._parameters.update({
                "displayName": None,
                "listOfParameters": None
            })
        elif type(parameters) is not dict or parameters == {}:
            raise TypeError("ParameterTypeError")
        else:
            for key, value in parameters.items():
                if type(key) is not str or type(value) is not str:
                    raise TypeError("ParameterTypeError")
            self._parameters = parameters
