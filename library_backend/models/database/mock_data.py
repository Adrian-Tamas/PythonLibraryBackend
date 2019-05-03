from library_backend.models.database.books_db_model import BooksDBModel
from library_backend.models.database.users_db_model import UsersDBModel

books = [BooksDBModel(name="A song of ice and fire", author="George R.R. Martin"),
         BooksDBModel(name="Nightflyers", author="George R.R. Martin"),
         BooksDBModel(name="Horus Heresy: Horus Rising", author="Dan Abnett"),
         BooksDBModel(name="Horus Heresy: False Gods", author="Graham McNeil"),
         BooksDBModel(name="Horus Heresy: Galaxy In Flames", author="Ben Counter"),
         BooksDBModel(name="Horus Heresy: The Flight of The Eisenstein", author="James Swallow"),
         BooksDBModel(name="Horus Heresy: Fulgrim", author="Graham McNeil"),
         BooksDBModel(name="Horus Heresy: Descent of Angels", author="Mitchell Scanlon"),
         BooksDBModel(name="Horus Heresy: Legion", author="Dan Abnett"),
         BooksDBModel(name="Horus Heresy: Battle for the Abyss", author="Ben Counter"),
         BooksDBModel(name="Horus Heresy: Mechanicum", author="Graham McNeil"),
         BooksDBModel(name="Horus Heresy: Tales of Heresy ",author="Nick Kyme and Lindsey Preistley"),
         BooksDBModel(name="Horus Heresy: Fallen Angels", author="Mike Lee"),
         BooksDBModel(name="Horus Heresy: A Thousand Sons", author="Graham McNeil"),
         BooksDBModel(name="Horus Heresy: Nemesis", author="James Swallow"),
         BooksDBModel(name="Horus Heresy: The First Heretic", author="Aaron Dembski-Bowden"),
         BooksDBModel(name="Horus Heresy: Prospero Burns", author="Dan Abnett"),
         BooksDBModel(name="Horus Heresy: Age Of Darkness", author="Christian Dunn"),
         BooksDBModel(name="Horus Heresy: The Outcast Dead", author="Graham McNeill"),
         BooksDBModel(name="Horus Heresy: Deliverance Lost", author="Gav Thorpe"),
         BooksDBModel(name="Horus Heresy: Know No Fear", author="Dan Abnett"),
         BooksDBModel(name="Horus Heresy: The Primarchs", author="Christian Dunn"),
         BooksDBModel(name="Horus Heresy: Fear To Tread", author="James Swallow"),
         BooksDBModel(name="Horus Heresy: Shadows Of Treachery",
                      author="Christian Dunn and Nick Kyme"),
         BooksDBModel(name="Horus Heresy: Angel Exterminatus", author="Graham McNeill"),
         BooksDBModel(name="Horus Heresy: Betrayer", author="Aaron Dembski-Bowden"),
         BooksDBModel(name="Horus Heresy: Mark Of Calth", author="Laurie Goulding"),
         BooksDBModel(name="Horus Heresy: Vulkan Lives", author="Nick Kyme"),
         BooksDBModel(name="Horus Heresy: The Unremembered Empire", author="Dan Abnett"),
         BooksDBModel(name="Horus Heresy: Scars ", author="Chris Wraight"),
         BooksDBModel(name="Horus Heresy: Vengeful Spirit", author="Graham McNeill"),
         BooksDBModel(name="Horus Heresy: The Damnation of Pythos", author="David Annandale")]

users_dict = [
    {
        "email": "ut@ornareIn.co.uk",
        "first_name": "Merrill",
        "last_name": "Mcdonald"
    },
    {
        "email": "tellus.Nunc.lectus@habitantmorbitristique.com",
        "first_name": "Fritz",
        "last_name": "Watts"
    },
    {
        "email": "lorem.luctus.ut@sagittis.com",
        "first_name": "Madison",
        "last_name": "Singleton"
    },
    {
        "email": "Sed.molestie.Sed@duiFuscealiquam.edu",
        "first_name": "Stephanie",
        "last_name": "Salas"
    },
    {
        "email": "orci@Integervitaenibh.net",
        "first_name": "Ethan",
        "last_name": "Larson"
    },
    {
        "email": "erat@PhasellusornareFusce.org",
        "first_name": "Giacomo",
        "last_name": "Mason"
    },
    {
        "email": "eu@mollisnon.net",
        "first_name": "Erica",
        "last_name": "Foley"
    },
    {
        "email": "ultrices@Fuscemollis.edu",
        "first_name": "Len",
        "last_name": "Woodard"
    },
    {
        "email": "risus.quis@quamCurabiturvel.net",
        "first_name": "Preston",
        "last_name": "Norman"
    },
    {
        "email": "gravida.nunc@necquamCurabitur.com",
        "first_name": "Ross",
        "last_name": "Bright"
    },
    {
        "email": "sodales.Mauris.blandit@ipsum.org",
        "first_name": "Nash",
        "last_name": "Munoz"
    },
    {
        "email": "sit.amet@estac.net",
        "first_name": "Jack",
        "last_name": "Rice"
    },
    {
        "email": "Morbi.vehicula@nunc.org",
        "first_name": "Victor",
        "last_name": "Anthony"
    },
    {
        "email": "convallis.erat@necmalesuadaut.org",
        "first_name": "Halee",
        "last_name": "Witt"
    },
    {
        "email": "Vivamus.rhoncus.Donec@acmieleifend.edu",
        "first_name": "Lareina",
        "last_name": "Vang"
    },
    {
        "email": "Vestibulum.ante.ipsum@auctor.co.uk",
        "first_name": "Leslie",
        "last_name": "Galloway"
    },
    {
        "email": "pede.malesuada.vel@nunc.com",
        "first_name": "Jael",
        "last_name": "King"
    },
    {
        "email": "tincidunt.neque.vitae@elitCurabitur.net",
        "first_name": "Nehru",
        "last_name": "Mullins"
    },
    {
        "email": "et.ultrices.posuere@nonloremvitae.com",
        "first_name": "Magee",
        "last_name": "Boone"
    },
    {
        "email": "velit.eu.sem@aliquamadipiscinglacus.org",
        "first_name": "Anika",
        "last_name": "Lott"
    },
    {
        "email": "enim.Curabitur@mauris.net",
        "first_name": "Clarke",
        "last_name": "Atkins"
    },
    {
        "email": "mattis@lobortisquama.co.uk",
        "first_name": "Valentine",
        "last_name": "Sanders"
    },
    {
        "email": "non@tempus.ca",
        "first_name": "Amanda",
        "last_name": "Allen"
    },
    {
        "email": "accumsan.neque.et@Nullasempertellus.edu",
        "first_name": "Vance",
        "last_name": "Brooks"
    },
    {
        "email": "amet.risus@risusquisdiam.com",
        "first_name": "Chelsea",
        "last_name": "Stevenson"
    },
    {
        "email": "Duis.dignissim@estacmattis.net",
        "first_name": "Kamal",
        "last_name": "Jarvis"
    },
    {
        "email": "Sed@velit.org",
        "first_name": "May",
        "last_name": "Bradshaw"
    },
    {
        "email": "Phasellus@Nam.ca",
        "first_name": "Benedict",
        "last_name": "Fletcher"
    },
    {
        "email": "elit@sociisnatoquepenatibus.ca",
        "first_name": "Silas",
        "last_name": "Baker"
    },
    {
        "email": "lacus.Etiam@neque.edu",
        "first_name": "Davis",
        "last_name": "Pugh"
    },
    {
        "email": "orci.consectetuer@nibhdolornonummy.edu",
        "first_name": "Warren",
        "last_name": "Peck"
    },
    {
        "email": "massa.Integer.vitae@quislectusNullam.co.uk",
        "first_name": "Nathaniel",
        "last_name": "Carroll"
    },
    {
        "email": "arcu.Morbi@Quisqueimperdieterat.ca",
        "first_name": "Reuben",
        "last_name": "Huber"
    },
    {
        "email": "odio.Aliquam.vulputate@tortorIntegeraliquam.org",
        "first_name": "Judah",
        "last_name": "Thompson"
    },
    {
        "email": "dolor.dolor@vestibulummassa.ca",
        "first_name": "Nigel",
        "last_name": "Justice"
    },
    {
        "email": "non.lacinia.at@consectetuereuismodest.edu",
        "first_name": "Ryder",
        "last_name": "Jennings"
    },
    {
        "email": "amet@et.com",
        "first_name": "Iliana",
        "last_name": "Le"
    },
    {
        "email": "vitae.velit@Nuncquisarcu.com",
        "first_name": "Kenyon",
        "last_name": "Best"
    },
    {
        "email": "est@necenimNunc.co.uk",
        "first_name": "Grace",
        "last_name": "Raymond"
    },
    {
        "email": "bibendum.ullamcorper@Sedmalesuadaaugue.edu",
        "first_name": "Tara",
        "last_name": "Bradshaw"
    },
    {
        "email": "et.libero@adipiscingfringilla.ca",
        "first_name": "Reece",
        "last_name": "Hanson"
    },
    {
        "email": "Sed.eu@diamPellentesquehabitant.org",
        "first_name": "Rachel",
        "last_name": "Petersen"
    },
    {
        "email": "eget.ipsum@egestas.com",
        "first_name": "Zena",
        "last_name": "Thornton"
    },
    {
        "email": "eleifend@faucibus.com",
        "first_name": "Jaden",
        "last_name": "Bullock"
    },
    {
        "email": "at@utsemNulla.org",
        "first_name": "Jescie",
        "last_name": "Petersen"
    },
    {
        "email": "Fusce.fermentum.fermentum@pharetraNamac.net",
        "first_name": "Orla",
        "last_name": "Evans"
    },
    {
        "email": "eleifend.Cras.sed@eu.org",
        "first_name": "Derek",
        "last_name": "Ryan"
    },
    {
        "email": "Fusce.aliquet@ametconsectetuer.ca",
        "first_name": "Venus",
        "last_name": "Dorsey"
    },
    {
        "email": "odio.semper@orciconsectetuereuismod.ca",
        "first_name": "Kylan",
        "last_name": "Fowler"
    },
    {
        "email": "fermentum.vel.mauris@orciPhasellus.com",
        "first_name": "Lucas",
        "last_name": "Lane"
    },
    {
        "email": "fermentum@a.net",
        "first_name": "Keith",
        "last_name": "Sherman"
    },
    {
        "email": "dui@Maurismolestie.org",
        "first_name": "Abel",
        "last_name": "Dalton"
    },
    {
        "email": "Integer@Mauris.org",
        "first_name": "Quemby",
        "last_name": "Cunningham"
    },
    {
        "email": "Donec.nibh@nonleoVivamus.edu",
        "first_name": "Isadora",
        "last_name": "Graham"
    },
    {
        "email": "aliquam@rutrum.com",
        "first_name": "Nicholas",
        "last_name": "Nielsen"
    },
    {
        "email": "eu@pellentesquea.ca",
        "first_name": "Francis",
        "last_name": "Alvarado"
    },
    {
        "email": "sed@Duis.ca",
        "first_name": "Hillary",
        "last_name": "Mcclure"
    },
    {
        "email": "ornare.libero@fringilla.org",
        "first_name": "Andrew",
        "last_name": "Bean"
    },
    {
        "email": "ut.pellentesque@et.org",
        "first_name": "Colton",
        "last_name": "Matthews"
    },
    {
        "email": "eu.tellus.eu@sagittislobortismauris.edu",
        "first_name": "Shellie",
        "last_name": "Callahan"
    },
    {
        "email": "et.magna@nonante.net",
        "first_name": "Drake",
        "last_name": "Brooks"
    },
    {
        "email": "primis.in.faucibus@sagittis.ca",
        "first_name": "Kimberley",
        "last_name": "Good"
    },
    {
        "email": "adipiscing@luctus.edu",
        "first_name": "Margaret",
        "last_name": "Rutledge"
    },
    {
        "email": "Aliquam.ultrices@milorem.edu",
        "first_name": "Driscoll",
        "last_name": "Burks"
    },
    {
        "email": "id.libero@Vivamus.ca",
        "first_name": "Kato",
        "last_name": "Dixon"
    },
    {
        "email": "ac.arcu.Nunc@nascetur.ca",
        "first_name": "Jared",
        "last_name": "Valencia"
    },
    {
        "email": "est.Nunc@Sedauctorodio.com",
        "first_name": "Cole",
        "last_name": "Quinn"
    },
    {
        "email": "turpis.egestas.Aliquam@molestie.net",
        "first_name": "Adrian",
        "last_name": "Dotson"
    },
    {
        "email": "pede.malesuada.vel@SuspendisseeleifendCras.edu",
        "first_name": "Geoffrey",
        "last_name": "Gould"
    },
    {
        "email": "Nunc@ligulaeu.org",
        "first_name": "Nero",
        "last_name": "Stout"
    },
    {
        "email": "quis.diam@Sed.edu",
        "first_name": "Reuben",
        "last_name": "Velez"
    },
    {
        "email": "Aliquam@temporbibendumDonec.edu",
        "first_name": "Keaton",
        "last_name": "Contreras"
    },
    {
        "email": "ut.cursus@mus.ca",
        "first_name": "Leilani",
        "last_name": "Forbes"
    },
    {
        "email": "faucibus.orci.luctus@Loremipsumdolor.co.uk",
        "first_name": "Kyra",
        "last_name": "Hays"
    },
    {
        "email": "Nunc@vel.ca",
        "first_name": "Merrill",
        "last_name": "Hammond"
    },
    {
        "email": "sapien.gravida.non@sedorcilobortis.com",
        "first_name": "Farrah",
        "last_name": "Daniels"
    },
    {
        "email": "ante.iaculis@aliquamiaculis.co.uk",
        "first_name": "Bruce",
        "last_name": "Gardner"
    },
    {
        "email": "nascetur.ridiculus@non.org",
        "first_name": "Sybil",
        "last_name": "Trevino"
    },
    {
        "email": "Aenean.massa@blandit.co.uk",
        "first_name": "Priscilla",
        "last_name": "Conley"
    },
    {
        "email": "Fusce@metus.org",
        "first_name": "Leslie",
        "last_name": "Hansen"
    },
    {
        "email": "venenatis@venenatislacusEtiam.org",
        "first_name": "Hakeem",
        "last_name": "Everett"
    },
    {
        "email": "non@justonecante.com",
        "first_name": "Rylee",
        "last_name": "Mcleod"
    },
    {
        "email": "eu.arcu.Morbi@semper.edu",
        "first_name": "Oleg",
        "last_name": "Ferrell"
    },
    {
        "email": "semper.auctor.Mauris@lacusQuisqueimperdiet.edu",
        "first_name": "Abel",
        "last_name": "Villarreal"
    },
    {
        "email": "eu.neque.pellentesque@Integer.ca",
        "first_name": "Mohammad",
        "last_name": "Buckner"
    },
    {
        "email": "nascetur@tellusfaucibusleo.com",
        "first_name": "Moses",
        "last_name": "Simpson"
    },
    {
        "email": "ut.odio@arcuSed.co.uk",
        "first_name": "Ryan",
        "last_name": "Cortez"
    },
    {
        "email": "vestibulum.lorem.sit@NullamenimSed.edu",
        "first_name": "Colleen",
        "last_name": "Russo"
    },
    {
        "email": "volutpat@eget.net",
        "first_name": "Keegan",
        "last_name": "Lawrence"
    },
    {
        "email": "ad.litora@nulla.com",
        "first_name": "Neville",
        "last_name": "Leach"
    },
    {
        "email": "euismod@pretium.ca",
        "first_name": "Callie",
        "last_name": "Hess"
    },
    {
        "email": "semper.dui@malesuadaInteger.edu",
        "first_name": "Keith",
        "last_name": "Baldwin"
    },
    {
        "email": "at.pede.Cras@dictum.co.uk",
        "first_name": "Ciara",
        "last_name": "Cunningham"
    },
    {
        "email": "Quisque.fringilla.euismod@sitametorci.edu",
        "first_name": "Claudia",
        "last_name": "Webb"
    },
    {
        "email": "arcu@orciluctus.net",
        "first_name": "Herman",
        "last_name": "Ferrell"
    },
    {
        "email": "Cum@consectetuercursus.net",
        "first_name": "Myles",
        "last_name": "Harvey"
    },
    {
        "email": "sollicitudin@sit.net",
        "first_name": "Lisandra",
        "last_name": "Bates"
    },
    {
        "email": "rhoncus.Donec@aliquetodioEtiam.com",
        "first_name": "Kelly",
        "last_name": "Russell"
    },
    {
        "email": "nunc@vestibulum.net",
        "first_name": "Julian",
        "last_name": "Jackson"
    },
    {
        "email": "egestas.a@pellentesque.com",
        "first_name": "Leandra",
        "last_name": "Case"
    }
]


def get_users_list():
    users = []

    for user_dict in users_dict:
        users.append(UsersDBModel(**user_dict))

    return users
