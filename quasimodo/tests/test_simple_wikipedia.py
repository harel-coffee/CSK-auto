import unittest

from quasimodo.inputs import Inputs
from quasimodo.generated_fact import GeneratedFact
from quasimodo.multiple_scores import MultipleScore
from quasimodo.multiple_source_occurrence import MultipleSourceOccurrence
from quasimodo.simple_wikipedia_cooccurrence_submodule import SimpleWikipediaCooccurrenceSubmodule


class TestSimpleWikipediaCooccurrence(unittest.TestCase):

    def setUp(self) -> None:
        self.simple_wikipedia_no_cache = SimpleWikipediaCooccurrenceSubmodule(None, False)
        self.empty_input = Inputs()

    def test_lion(self):
        generated_fact = GeneratedFact("lion", "is a", "cat", "", False, MultipleScore(), MultipleSourceOccurrence())
        inputs = self.empty_input.add_generated_facts([generated_fact])
        inputs = self.simple_wikipedia_no_cache.process(inputs)
        self.assertEqual(1, len(inputs.get_generated_facts()))
        scores = inputs.get_generated_facts()[0].get_score()
        scores_wikipedia = [x for x in scores.scores if x[2].get_name() == "Simple Wikipedia Cooccurrence"]
        self.assertEqual(1, len(scores_wikipedia))
        self.assertTrue(scores_wikipedia[0][0] != 0)

    def test_cache(self):
        wikipedia_cache = SimpleWikipediaCooccurrenceSubmodule(None, True, "simple-wikipedia-cache-test")
        generated_fact = GeneratedFact("lion", "is a", "cat", "", False, MultipleScore(), MultipleSourceOccurrence())
        inputs = self.empty_input.add_generated_facts([generated_fact])
        wikipedia_cache.process(inputs)
        generated_fact = GeneratedFact("lion", "is a", "cat", "", False, MultipleScore(), MultipleSourceOccurrence())
        inputs = self.empty_input.add_generated_facts([generated_fact])
        inputs = wikipedia_cache.process(inputs)
        self.assertEqual(1, len(inputs.get_generated_facts()))
        scores = inputs.get_generated_facts()[0].get_score()
        scores_wikipedia = [x for x in scores.scores if x[2].get_name() == "Simple Wikipedia Cooccurrence"]
        self.assertEqual(1, len(scores_wikipedia))
        self.assertTrue(scores_wikipedia[0][0] != 0)
        wikipedia_cache.cache.delete_cache()


if __name__ == '__main__':
    unittest.main()
