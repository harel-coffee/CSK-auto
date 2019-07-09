from quasimodo.serializable import Serializable
from .generated_fact_interface import GeneratedFactInterface
from .subject import Subject
from .object import Object
from .predicate import Predicate
from .modality import Modality
from .fact import Fact


class GeneratedFact(GeneratedFactInterface, Serializable):
    """GeneratedFact
    The default implementation of GeneratedFactInterface
    """

    def to_dict(self):
        res = dict()
        res["type"] = "GeneratedFact"
        res["subject"] = self._subject.to_dict()
        res["predicate"] = self._predicate.to_dict()
        res["object"] = self._object.to_dict()
        if self._modality is not None:
            res["modality"] = self._modality.to_dict()
        else:
            res["modality"] = {"type": "NO_MODALITY"}
        res["negative"] = self._negative
        res["score"] = self._score.to_dict()
        res["sentence_source"] = self._sentence_source
        if self._pattern is not None:
            res["pattern"] = self._pattern.to_dict()
        else:
            res["pattern"] = {"type": "NO_PATTERN"}
        return res

    def __init__(self, subject, predicate, obj, modality, negative, score, sentence_source, pattern=None):
        super().__init__()
        if type(subject) == str:
            self._subject = Subject(subject)
        else:
            self._subject = subject # SubjectInterface
        if type(predicate) == str:
            self._predicate = Predicate(predicate)
        else:
            self._predicate = predicate # PredicateInterface
        if type(obj) == str:
            self._object = Object(obj)
        else:
            self._object = obj # ObjectInterface
        if type(modality) == str:
            self._modality = Modality(modality)
        else:
            self._modality = modality # Optional ModalityInterface
        self._negative = negative
        self._score = score
        self._sentence_source = sentence_source
        self._pattern = pattern

    def get_fact(self):
        return Fact(self.get_subject(),
                    self.get_predicate(),
                    self.get_object(),
                    self.get_modality(),
                    self.is_negative())

    def change_subject(self, new_subject):
        return GeneratedFact(new_subject,
                             self.get_predicate(),
                             self.get_object(),
                             self.get_modality(),
                             self.is_negative(),
                             self.get_score(),
                             self.get_sentence_source(),
                             self.get_pattern())

    def change_predicate(self, new_predicate):
        return GeneratedFact(self.get_subject(),
                             new_predicate,
                             self.get_object(),
                             self.get_modality(),
                             self.is_negative(),
                             self.get_score(),
                             self.get_sentence_source(),
                             self.get_pattern())

    def change_object(self, new_object):
        return GeneratedFact(self.get_subject(),
                             self.get_predicate(),
                             new_object,
                             self.get_modality(),
                             self.is_negative(),
                             self.get_score(),
                             self.get_sentence_source(),
                             self.get_pattern())

    def change_modality(self, new_modality):
        return GeneratedFact(self.get_subject(),
                             self.get_predicate(),
                             self.get_object(),
                             new_modality,
                             self.is_negative(),
                             self.get_score(),
                             self.get_sentence_source(),
                             self.get_pattern())

    def change_score(self, new_score):
        """change_score
        Change the score of the generated fact
        :param new_score: the new score to put
        :type new_score: Float
        :return: A generated fact with the new score
        :rtype: GeneratedFactInterface
        """
        return GeneratedFact(self.get_subject(),
                             self.get_predicate(),
                             self.get_object(),
                             self.get_modality(),
                             self.is_negative(),
                             new_score,
                             self.get_sentence_source(),
                             self.get_pattern())

    def change_pattern(self, new_pattern):
        return GeneratedFact(self.get_subject(),
                             self.get_predicate(),
                             self.get_object(),
                             self.get_modality(),
                             self.is_negative(),
                             self.get_score(),
                             self.get_sentence_source(),
                             new_pattern)

    def change_sentence(self, new_sentence):
        return GeneratedFact(self.get_subject(),
                             self.get_predicate(),
                             self.get_object(),
                             self.get_modality(),
                             self.is_negative(),
                             self.get_score(),
                             new_sentence,
                             self.get_pattern())

    def remove_sentence(self):
        return GeneratedFact(self.get_subject(),
                             self.get_predicate(),
                             self.get_object(),
                             self.get_modality(),
                             self.is_negative(),
                             self.get_score(),
                             "",
                             self.get_pattern())
