from .module_interface import ModuleInterface
from .default_submodule_factory import DefaultSubmoduleFactory
import logging


class AssertionNormalizationModule(ModuleInterface):
    """AssertionNormalizationModule
    A class to normalize the assertion generated by other modules
    """

    def __init__(self):
        module_names = ["lower-case", "only-subject", "no-personal", "singular-subject",
                        "cleaning-predicate", "basic-modality",
                        "present-continuous", "are-transformation",
                        "can-transformation", "filter-object",
                        "be-normalization",
                        "identical-subj-obj",
                        "fact-combinor"]
        super(AssertionNormalizationModule, self).__init__(
            module_names, DefaultSubmoduleFactory())
        self._name = "Assertion Normalization Module"

    def process(self, input_interface):
        logging.info("Start the assertion normalization module")
        for submodule in self._submodules:
            input_interface = submodule.process(input_interface)
        return input_interface