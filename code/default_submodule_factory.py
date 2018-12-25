from submodule_factory_interface import SubmoduleFactoryInterface
from submodule_google_autocomplete import SubmoduleGoogleAutocomplete
from animal_submodule import AnimalSubmodule
from manual_patterns_google_submodule import ManualPatternsGoogleSubmodule
from bing_autocomplete_submodule import BingAutocompleteSubmodule
from only_subject_submodule import OnlySubjectSubmodule
from no_personal_submodule import NoPersonalSubmodule
from linear_combination_submodule import LinearCombinationSubmodule
from linear_combination_weighted_submodule import LinearCombinationWeightedSubmodule
from to_singular_subject_submodule import ToSingularSubjectSubmodule
from present_continuous_submodule import PresentContinuousSubmodule
from basic_modality_submodule import BasicModalitySubmodule
from cleaning_predicate_submodule import CleaningPredicateSubmodule
from wikipedia_cooccurrence_submodule import WikipediaCooccurrenceSubmodule
from simple_wikipedia_cooccurrence_submodule import SimpleWikipediaCooccurrenceSubmodule
from antonym_checking_submodule import AntonymCheckingSubmodule
from are_transformation_submodule import AreTransformationSubmodule
from filter_object_submodule import FilterObjectSubmodule
from can_transformation_submodule import CanTransformationSubmodule
from incomplete_modality_submodule import IncompleteModalitySubmodule
from occupations_submodule import OccupationsSubmodule
from conceptnet_subjects_submodule import ConceptnetSubjectsSubmodule
from be_normalization_submodule import BeNormalizationSubmodule
from reddit_questions_submodule import RedditQuestionsSubmodule
from conceptnet_seeds_submodule import ConceptNetSeedsSubmodule
from quora_questions_submodule import QuoraQuestionsSubmodule
from answerscom_questions_submodule import AnswerscomQuestionsSubmodule
from imagetag_submodule import ImagetagSubmodule
from flickr_clusters_submodule import FlickrClustersSubmodule


class DefaultSubmoduleFactory(SubmoduleFactoryInterface):
    """DefaultSubmoduleFactory
    The default submodule factory
    """

    def __init__(self):
        self._submodules = {
            "google-autocomplete": SubmoduleGoogleAutocomplete,
            "animal-seeds": AnimalSubmodule,
            "manual-patterns-google": ManualPatternsGoogleSubmodule,
            "bing-autocomplete": BingAutocompleteSubmodule,
            "only-subject": OnlySubjectSubmodule,
            "no-personal": NoPersonalSubmodule,
            "linear-combination": LinearCombinationSubmodule,
            "linear-combination-weighted": LinearCombinationWeightedSubmodule,
            "singular-subject": ToSingularSubjectSubmodule,
            "present-continuous": PresentContinuousSubmodule,
            "basic-modality": BasicModalitySubmodule,
            "cleaning-predicate": CleaningPredicateSubmodule,
            "wikipedia-cooccurrence": WikipediaCooccurrenceSubmodule,
            "simple-wikipedia-cooccurrence": SimpleWikipediaCooccurrenceSubmodule,
            "antonym-checking": AntonymCheckingSubmodule,
            "are-transformation": AreTransformationSubmodule,
            "filter-object": FilterObjectSubmodule,
            "can-transformation": CanTransformationSubmodule,
            "incomplete-modality": IncompleteModalitySubmodule,
            "occupations-seeds": OccupationsSubmodule,
            "conceptnet-subjects": ConceptnetSubjectsSubmodule,
            "be-normalization": BeNormalizationSubmodule,
            "reddit-questions": RedditQuestionsSubmodule,
            "quora-questions": QuoraQuestionsSubmodule,
            "conceptnet-seeds": ConceptNetSeedsSubmodule,
            "answerscom-questions": AnswerscomQuestionsSubmodule,
            "imagetag": ImagetagSubmodule,
            "flickr-clusters": FlickrClustersSubmodule
        }


    def get_submodule(self, submodule_name, module_reference):
        if submodule_name in self._submodules:
            return self._submodules[submodule_name](module_reference)
        else:
            raise NotImplementedError
