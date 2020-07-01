from OutputFlow.Surprises.SurpriseFrame import SurpriseFrame
from random import randrange


class Animals(SurpriseFrame):
    """
    This class is a surprise.
    it heritage from SurpriseFrame.
    the query that will returned form this surprise is a random animal
    in the first letter of the username's name
    the class has dict with all the animals, and it randomize from it first
    letter an animal.
    """
    DICT_ANIMALS = {
        'a': [
            "Aardvark",
            "Albatross",
            "Alligator",
            "Alpaca",
            "Ant",
            "Anteater",
            "Antelope",
            "Ape",
            "Armadillo"
        ],
        'b': [
            "Baboon",
            "Badger",
            "Barracuda",
            "Bat",
            "Bear",
            "Beaver",
            "Bee",
            "Bison",
            "Boar",
            "Buffalo",
            "Butterfly"
        ],
        'c': [
            "Camel",
            "Capybara",
            "Caribou",
            "Cassowary",
            "Cat",
            "Caterpillar",
            "Cattle",
            "Chamois",
            "Cheetah",
            "Chicken",
            "Chimpanzee",
            "Chinchilla",
            "Chough",
            "Clam",
            "Cobra",
            "Cockroach",
            "Cod",
            "Cormorant",
            "Coyote",
            "Crab",
            "Crane",
            "Crocodile",
            "Crow",
            "Curlew"
        ],
        'd': [
            "Deer",
            "Dinosaur",
            "Dog",
            "Donkey",
            "Dogfish",
            "Dolphin",
            "Dotterel",
            "Dove",
            "Dragonfly",
            "Duck",
            "Dugong",
            "Dunlin"
        ],
        'e': [
            "Eagle",
            "Echidna",
            "Eel",
            "Eland",
            "Elephant",
            "Elk",
            "Emu"
        ],
        'f': [
            "Falcon",
            "Ferret",
            "Finch",
            "Fish",
            "Flamingo",
            "Fly",
            "Fox",
            "Frog"
        ],
        'g': [
            "Gaur",
            "Gazelle",
            "Gerbil",
            "Giraffe",
            "Gnat",
            "Gnu",
            "Goat",
            "Goldfinch",
            "Goldfish",
            "Goose",
            "Gorilla",
            "Goshawk",
            "Grasshopper",
            "Grouse",
            "Guanaco",
            "Gull"
        ],
        'h': [
            "Hamster",
            "Hare",
            "Hawk",
            "Hedgehog",
            "Heron",
            "Herring",
            "Hippopotamus",
            "Hornet",
            "Horse",
            "Human",
            "Hummingbird",
            "Hyena"
        ],
        'i': [
            "Ibex",
            "Ibis"
        ],
        'j': [
            "Jackal",
            "Jaguar",
            "Jay",
            "Jellyfish"
        ],
        'k': [
            "Kangaroo",
            "Kingfisher",
            "Koala",
            "Kookabura",
            "Kouprey",
            "Kudu"
        ],
        'l': [
            "Lapwing",
            "Lark",
            "Lemur",
            "Leopard",
            "Lion",
            "Llama",
            "Lobster",
            "Locust",
            "Loris",
            "Louse",
            "Lyrebird"
        ],
        'm': [
            "Magpie",
            "Mallard",
            "Manatee",
            "Mandrill",
            "Mantis",
            "Marten",
            "Meerkat",
            "Mink",
            "Mole",
            "Mongoose",
            "Monkey",
            "Moose",
            "Mosquito",
            "Mouse",
            "Mule",
            "Narwhal"
        ],
        'n': [
            "Newt",
            "Nightingale"
        ],
        'p': [
            "Octopus",
            "Okapi",
            "Opossum",
            "Oryx",
            "Ostrich",
            "Otter",
            "Owl",
            "Oyster"
        ],
        'p': [
            "Panther",
            "Parrot",
            "Partridge",
            "Peafowl",
            "Pelican",
            "Penguin",
            "Pheasant",
            "Pig",
            "Pigeon",
            "Pony",
            "Porcupine",
            "Porpoise"
        ],
        'q': [
            "Quail",
            "Quelea",
            "Quetzal"
        ],
        'r': [
            "Rabbit",
            "Raccoon",
            "Rail",
            "Ram",
            "Rat",
            "Raven",
            "Red deer",
            "Red panda",
            "Reindeer",
            "Rhinoceros",
            "Rook"
        ],
        's': [
            "Salamander",
            "Salmon",
            "Sand Dollar",
            "Sandpiper",
            "Sardine",
            "Scorpion",
            "Seahorse",
            "Seal",
            "Shark",
            "Sheep",
            "Shrew",
            "Skunk",
            "Snail",
            "Snake",
            "Sparrow",
            "Spider",
            "Spoonbill",
            "Squid",
            "Squirrel",
            "Starling",
            "Stingray",
            "Stinkbug",
            "Stork",
            "Swallow",
            "Swan"
        ],
        't': [
            "Tapir",
            "Tarsier",
            "Termite",
            "Tiger",
            "Toad",
            "Trout",
            "Turkey",
            "Turtle"
        ],
        'v': [
            "Viper",
            "Vulture"
        ],
        'w': [
            "Wallaby",
            "Walrus",
            "Wasp",
            "Weasel",
            "Whale",
            "Wildcat",
            "Wolf",
            "Wolverine",
            "Wombat",
            "Woodcock",
            "Woodpecker",
            "Worm",
            "Wren"
        ],
        'y': [
            "Yak"
        ],
        'z': [
            "Zebra"
        ]
    }
    TYPE = 'animal in your first letter'

    def __init__(self):
        super().__init__()

    def get_query(self):
        """
        This method make the query- return a random animal in your first letter
        :return: string- joke of chuckNorris
        """
        first_ch = self.get_val(0)[0].lower()
        num_of_animals = len(self.DICT_ANIMALS[first_ch])
        return self.DICT_ANIMALS[first_ch][randrange(num_of_animals)]
