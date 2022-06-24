import classes


def guidelines():
    """
    Scrabble
    Εργασία στο μάθημα της Θεωρίες Μάθησης και Εκπαιδευτικό Λογισμικό
    Όνομα: Νάκας Αθανάσιος
    ΑΕΜ: 3588

    Η εργασία υλοποιήθηκε ατομικά.
    Ο κώδικας του κυρίου προγράμματος βρίσκεται στο main-3588.py, και ο κώδικας των κλάσεων που αναπτύχθηκαν στο αρχείο
    classes.py όπως αναφέρθηκε στην εκφώνηση. Επιλέχθηκε dictionary για την οργάνωση των λέξεων της γλώσσας γιατί
    βοηθάει στον χρόνο εύρεσης λέξεων, αλλά και στην γενική εκτέλεση του κώδικα. Επιλέχθηκε να υλοποιηθεί ο αλγόριθμος:
    ΑΛΓΟΡΙΘΜΟΣ 1 Min-Max-Smart, για να παίξει ο Η/Υ. Δεν υλοποίησα υπερφόρτωση τελεστών. Xρησιμοποίησα 3 static method
    decorators (@staticmethod) στον κώδικα (classes.py line: 147, 462, 485).

    Κλάσεις:
    1) Sakclass
        Βασική κλάση
        Attributes:
            - sack: public list,  χρησιμοποιείται για την αποθήκευση τωρινού αριθμού γραμμάτων που απομένουν
            για κάθε γράμμα
            - __Values_of_Letters: private dictionary, περιέχει κάθε γράμμα και το πόσους πόντους δίνει
            - __Number_of_Letters: private dictionary, περιέχει κάθε γράμμα και το πόσες φορές μπορεί να
            υπάρχει στο "σακουλάκι"
            - __Letters: private list, περιέχει όλα τα ελληνικά κεφαλαία γράμματα
        Methods:
            - __init__(self): private method, constructor της κλάσης, χρησιμοποιείται για αρχικοποίηση των attributes
            - __randomize_sak(self): private method, καλείται από τον constructor, και "γεμίζει" το attribute sack με τα
            γράμματα
            - get_letters(self): public method, Getter για το list Letters
            - get_letter_point(self, letter): public method, επιστρέφει τους πόντους που δίνει το γράμμα letter που
            δίνεται ως όρισμα
            - word_exists(self, word): public method, ελέγχει εάν τα γράμματα της λέξης word που δίνεται ως όρισμα
            υπάρχουν στην λίστα των γραμμάτων, εάν η λέξη word υπάρχει στο dictionary από τις λέξεις που υπάρχουν στο
            greek7.txt και επιστρέφει την κατάλληλη boolean τιμή
            - getletters(self, n): public method, δημιουργεί ένα list n τυχαία επιλεγμένων γραμμάτων από το sack και
            επιστρέφει
            - putbackletters(self, letters): public method, επιστρέφει στο sack τα γράμματα που περιέχονται στο list
            letters
            - get_num_remaining(self): public method, επιστρέφει το άθροισμα του αριθμού των γραμμάτων που υπάρχουν στο
            sack
    2) Player:
        Βασική κλάση
        Attributes:
            - _letters, protected list, χρησιμοποιείται για την αποθήκευση των γραμμάτων που έχει στην διάθεση του
            ο παίκτης
            - _points, protected int, χρησιμοποιείται για την αποθήκευση των πόντων του παίκτη
            - _sak, protected object της κλάσης Sakclass(), χρησιμοποιείται για την αποθήκευση του instance
            της SakClass
        Methods:
            - __init__(self): private method, constructor της κλάσης, χρησιμοποιείται για αρχικοποίηση των attributes
            - __repr__(self): private method, χρησιμοποιείται για την δημιουργία αναπαράστασης του αντικειμένου
            - set_letters(self, letters): public method, χρησιμοποιείται για να ορίσει τα γράμματα του list του παίκτη
            σε αυτά του list letters
            - reroll_letters(self, sak, temp_letters): public method, χρησιμοποιείται για να κάνει reroll τα γράμματα
            του χρήστη. Εάν υπάρχουν τουλάχιστον 7 γράμματα στο sak τα αντικαθιστεί με 7 καινούργια, εάν έχει λιγότερα
            από 7 και περισσότερα από 2 τα αντικαθιστεί με όσα παραμένουν και εάν έχει μόνο ένα επιστρέφει False επειδή
            δεν μπόρεσε να ολοκληρωθεί η διαδικασία. Στις δύο πρώτες περιπτώσεις επιστρέφει True
            - add_points(self, word, temp_letters): public method, χρησιμοποιείται για πρόσθεση των πόντων του παίκτη
            και συμπλήρωση των γραμμάτων του ανάλογα με το πόσα παραμένουν στο sak. Εάν είναι αρκετά για συμπληρώσουν 7
            συμπληρώνονται, εάν δεν είναι αρκετά για 7 αλλά είναι περισσότερα από δύο συμπληρώνονται με όσα παραμένουν,
            αλλιώς αν δηλαδή είναι μόνο ένα επιστρέφεται False. Στις δύο πρώτες περιπτώσεις επιστρέφεται True. Εκτός από
            την Boolean μεταβλητή επιστρέφεται και ο αριθμός των πόντων για να χρησιμοποιηθεί στα σχετικά μηνύματα
            - check_remaining_letters(self, sak, number): public method, χρησιμοποιείται για να ελεγχθεί εάν υπάρχουν
            λιγότερα γράμματα στο sak από τον number attribute που δίνεται. Επιστρέφει boolean τιμή ανάλογα την
            περίπτωση καθώς και τον αριθμό γραμμάτων που παραμένουν στο sak
            - check_valid_word_existence(self): public method, χρησιμοποιείται για να ελέγχει εάν υπάρχει έγκυρη επιλογή
            λέξης με τα γράμματα που έχει ο χρήστης και επιστρέφει κατάλληλη boolean τιμή
            - get_letters(self): public method, getter για τo list των γραμμάτων του παίκτη
            - get_points(self):public method, getter για τους πόντους του παίκτη
            - form_answer(sak, letters, player): χρησιμοποιείται για τον σχηματισμό μηνύματος διαθέσιμων γραμμάτων βάση
            το είδος του παίκτη
    3) Human:
        Παράγωγη της Player
        Attibute:
            - __temp_letters: private attribute, χρησιμοποιείται για προσωρινή αποθήκευση των γραμμάτων του παίκτη σε
            ορισμένες μεθόδους
        Methods:
            - __init__(self): private method, constructor της κλάσης, χρησιμοποιείται για κλήση του parent constructor
            και αρχικοποίηση των attributes
            - play(self, sak): public method, χρησιμοποιείται για την εκτέλεση της σειράς του ανθρώπου-παίκτη. Εμφανίζει
            κατάλληλο μύνημα και περιμένει input από τον χρήστη με λέξη ή με το γράμμα από συγκεκριμένο option από τα
            παρακάτω:
            "p": re-roll
            "q": quit
            "c": έλεγχος εάν υπάρχει δυνατή λέξη με τα γράμματα του χρήστη
            "h": help, οδηγεί σε αυτές της εντολές (μπορούν να πατηθούν και χωρίς την χρήση του help)
            Εάν δωθεί λέξει από τον χρήστη, ελέγχεται εάν είναι σωστή και βγάζει σχετικά μυνήματα, όπως και στην
            περίπτωση μη έγκυρου input
            - __validate_word(self, word): private method, χρησιμοποιείται για να ελεγχθεί εάν ο χρήστης χρησιμοποίεισαι
            μόνο γράμματα που έχει στην διάθεση του με χρήση του temp_letters που αναφέρθηκε και παραπάνω. Επιστρέφεται
            κατάλληλη boolean τιμή βάση του ελέγχου
    4) Computer
        Παράγωγη της Player
        Attibute:
            - __temp_letters: private attribute, χρησιμοποιείται για προσωρινή αποθήκευση των γραμμάτων του παίκτη σε
            ορισμένες μεθόδους
            - __mode: private attribute, χρησιμοποιείται για αποθήκευση του mode, δηλαδή του αλγορίθμου που θα
            χρησιμοποιηθεί για την σειρά του υπολογιστή
        Methods:
            - __init__(self): private method, constructor της κλάσης, χρησιμοποιείται για κλήση του parent constructor
            και αρχικοποίηση των attributes
            - play(self, sak, mode): public method, χρησιμοποιείται για την εκτέλεση της σειράς του υπολογιστή-παίκτη.
            Καλεί την κατάλληλη μέθοδο από τους αλγόριθμους βάση του mode
            - __min_mode(self): private method, υλοποίηση του MIN αλγορίθμου. Αρχικά ελέγχει εάν υπάρχει έγκυρη με τα
            γράμματα του υπολογιστή. Εάν όχι κάνει re-roll. Εάν και πάλι δεν υπάρχει επιστρέφεται False επειδή δεν
            μπόρεσε να ολοκληρωθεί ο αλγόριθμος. Σε κάθε άλλη περίπτωση δημιουργεί όλα τα permutations με τα γράμματα
            του υπολογιστή ξεκινώντας από 2 και κρατάει την πρώτη αποδεκτή λέξη. Προσθέτει του πόντους, βγάζει σχετικό
            μήνυμα και επιστρέφει True. Εάν δεν υπάρχουν αρκετά γράμματα για συμπλήρωση επιστρέφει False
            - __max_mode(self): private method, υλοποίηση του MAX αλγορίθμου. Λειτουργεί, όπως ο min με μόνη διαφορά ότι
            ξεκινάει τα permutations από των αριθμό των γραμμάτων που έχει ο υπολογιστής.
            - __smart_mode(self): private method, υλοποίηση του SMART αλγορίθμου. Όπως οι δύο προηγούμενες, με μόνη
            διαφορά ότι κάνει όλα τα permutations και επιλέγει την λέξη με οδηγεί στους περισσότερους πόντους
    5) Game
        Βασική κλάση
        Attribute:
            - __modes: private list, περιέχει όλα τα διαθέσιμα modes-αλγόριθμους
            - __current_mode: private str, περιέχει το τωρινό mode-αλγόριθμο, default είναι ο MIN
            - __score_file_path: private str, περιέχει το path για το αρχείο με τα Data από τα προηγούμενα game
            - __word_file_path: private str, περιέχει το path από το αρχείο greek7.txt
            - __sak: private object of the class SakClass
            - __player: private object of the class Human
            - __computer: private object of the class Computer
        Methods:
            - __init__(self): private method, constructor της κλάσης, χρησιμοποιείται για την αρχικοποίηση των
            attributes, και την κλήση της create_dictionary μεθόδου
            - __repr__(self): public method, χρησιμοποιείται για την δημιουργία αναπαράστασης του αντικειμένου
            - __setup(self): private method, χρησιμοποιείται για την αλλαγή του αλγορίθμου του υπολογιστή
            - run(self): public method, χρησιμοποιείται για την εκτέλεση του παιχνιδιού. Αρχικά δίνει στο παίκτη
            της παρακάτω επιλογές:
            "1: Start", η οποία ξεκινάει το παιχνίδι
            "2: Settings", η οποία εμφανίζει το setup menu καλώντας την __setup()
            "3: Previous Results", η οποία εμφανίζει τα προηγούμενα αποτελέσματα καλώντας την show_previous_results()
            "q: Quit" η οποία καλεί την __end()
            Όταν δωθεί 1 ή Start ως input τότε δίνονται γράμματα στον άνθρωπο-παίκτη, στον υπολογιστή-παίκτη με χρήση
            των μεθόδων που αναφέρθηκαν παραπάνω και ξεκινάει ένα loop με τους γύρους των παικτών μέχρι να επιστραφεί
            false από την μέθοδο play() ενός εκ των δύο, όπου καλείται η end()
            - __end(self): private method, ελέγχει ποιος από τους δυο παίκτες έχει περισσότερους πόντους, βγάζει σχετικό
            μήνυμα, αποθηκεύει το αποτέλεσμα στο αρχείο DataScoreFile.json καλώντας την __update_score_data() και
            ολοκληρώνει το πρόγραμμα
            - __show_previous_results(self): private method, χρησιμοποιεί την __load_score_data για να δει εάν το αρχείο
            με τα αποθηκευμένα αποτελέσματα είναι άδειο ή όχι και ανάλογα την περίπτωση επιστρέφει ότι δεν υπάρχουν
            προηγούμενα αποτελέσματα ή όλα τα προηγούμενα αποτελέσματα
            - __load_score_data(path): private method, χρησιμοποιείται για να ελεγχεί εάν το αρχείο με όνομα path είναι
            άδειο ή όχι. Εάν είναι άδειο επιστρέφει "Empty file", αλλιώς τα δεδομένα του αρχείου
            - __update_score_data(self, path, player_score, pc_score): private method, χρησιμοποιεί την
            __load_score_data για να δει εάν το αρχείο με τα αποθηκευμένα αποτελέμσατα είναι άδειο ή όχι και ανάλογα την
            περίπτωση αποθηκεύει το σκορ του ανθρώπου-παίκτη και του υπολογιστή-παίκτη στο αρχείο
            - __create_dictionary(path): private method, ανοίγει το αρχείο με όνομα path, διαβάζει μια μια τις
            γραμμές-λέξεις και τις αποθηκεύει στο λεξικό dictionary με βάση το πρώτο τους γράμμα
    """


game = classes.Game()
game.run()
