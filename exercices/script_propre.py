import unittest
from typing import List

MIN_NAME_LENGTH = 7


def count_names_longer_than(prenoms: List[str], min_length: int = MIN_NAME_LENGTH) -> int:
    count = 0
    for prenom in prenoms:
        if len(prenom) > min_length:
            print(f"{prenom} est un prénom avec un nombre de lettres supérieur à {min_length}")
            count += 1
        else:
            print(f"{prenom} est un prénom avec un nombre de lettres inférieur ou égal à {min_length}")
    return count


class TestCountNamesLongerThan(unittest.TestCase):

    def test_count_names_longer_than(self) -> None:
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_names_longer_than(prenoms=prenoms)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
