from random import randrange


def personality(options):
    # 234
    positive_traits = ['Accessible', 'Active', 'Adaptable', 'Admirable', 'Adventurous', 'Agreeable', 'Alert',
                       'Allocentric', 'Amiable', 'Anticipative', 'Appreciative', 'Articulate', 'Aspiring', 'Athletic',
                       'Attractive', 'Balanced', 'Benevolent', 'Brilliant', 'Calm', 'Capable', 'Captivating', 'Caring',
                       'Challenging', 'Charismatic', 'Charming', 'Cheerful', 'Clean', 'Clear-headed', 'Clever',
                       'Colorful', 'Companionly', 'Compassionate', 'Conciliatory', 'Confident', 'Conscientious',
                       'Considerate', 'Constant', 'Contemplative', 'Cooperative', 'Courageous', 'Courteous', 'Creative',
                       'Cultured', 'Curious', 'Daring', 'Debonair', 'Decent', 'Decisive', 'Dedicated', 'Deep',
                       'Dignified', 'Directed', 'Disciplined', 'Discreet', 'Dramatic', 'Dutiful', 'Dynamic', 'Earnest',
                       'Ebullient', 'Educated', 'Efficient', 'Elegant', 'Eloquent', 'Empathetic', 'Energetic',
                       'Enthusiastic', 'Esthetic', 'Exciting', 'Extraordinary', 'Fair', 'Faithful', 'Farsighted',
                       'Felicific', 'Firm', 'Flexible', 'Focused', 'Forecful', 'Forgiving', 'Forthright',
                       'Freethinking', 'Friendly', 'Fun-loving', 'Gallant', 'Generous', 'Gentle', 'Genuine',
                       'Good-natured', 'Gracious', 'Hardworking', 'Healthy', 'Hearty', 'Helpful', 'Herioc',
                       'High-minded', 'Honest', 'Honorable', 'Humble', 'Humorous', 'Idealistic', 'Imaginative',
                       'Impressive', 'Incisive', 'Incorruptible', 'Independent', 'Individualistic', 'Innovative',
                       'Inoffensive', 'Insightful', 'Insouciant', 'Intelligent', 'Intuitive', 'Invulnerable', 'Kind',
                       'Knowledge', 'Leaderly', 'Leisurely', 'Liberal', 'Logical', 'Lovable', 'Loyal', 'Lyrical',
                       'Magnanimous', 'Many-sided', 'Masculine  (Manly)', 'Mature', 'Methodical', 'Maticulous',
                       'Moderate', 'Modest', 'Multi-leveled', 'Neat', 'Nonauthoritarian', 'Objective', 'Observant',
                       'Open', 'Optimistic', 'Orderly', 'Organized', 'Original', 'Painstaking', 'Passionate', 'Patient',
                       'Patriotic', 'Peaceful', 'Perceptive', 'Perfectionist', 'Personable', 'Persuasive', 'Planful',
                       'Playful', 'Polished', 'Popular', 'Practical', 'Precise', 'Principled', 'Profound', 'Protean',
                       'Protective', 'Providential', 'Prudent', 'Punctual', 'Pruposeful', 'Rational', 'Realistic',
                       'Reflective', 'Relaxed', 'Reliable', 'Resourceful', 'Respectful', 'Responsible', 'Responsive',
                       'Reverential', 'Romantic', 'Rustic', 'Sage', 'Sane', 'Scholarly', 'Scrupulous', 'Secure',
                       'Selfless', 'Self-critical', 'Self-defacing', 'Self-denying', 'Self-reliant', 'Self-sufficent',
                       'Sensitive', 'Sentimental', 'Seraphic', 'Serious', 'Sexy', 'Sharing', 'Shrewd', 'Simple',
                       'Skillful', 'Sober', 'Sociable', 'Solid', 'Sophisticated', 'Spontaneous', 'Sporting', 'Stable',
                       'Steadfast', 'Steady', 'Stoic', 'Strong', 'Studious', 'Suave', 'Subtle', 'Sweet', 'Sympathetic',
                       'Systematic', 'Tasteful', 'Teacherly', 'Thorough', 'Tidy', 'Tolerant', 'Tractable', 'Trusting',
                       'Uncomplaining', 'Understanding', 'Undogmatic', 'Unfoolable', 'Upright', 'Urbane', 'Venturesome',
                       'Vivacious', 'Warm', 'Well-bred', 'Well-read', 'Well-rounded', 'Winning', 'Wise', 'Witty',
                       'Youthful']

    # 112
    neutral_traits = ['Absentminded', 'Aggressive', 'Ambitious', 'Amusing', 'Artful', 'Ascetic', 'Authoritarian',
                      'Big-thinking', 'Boyish', 'Breezy', 'Businesslike', 'Busy', 'Casual', 'Crebral', 'Chummy',
                      'Circumspect', 'Competitive', 'Complex', 'Confidential', 'Conservative', 'Contradictory',
                      'Crisp', 'Cute', 'Deceptive', 'Determined', 'Dominating', 'Dreamy', 'Driving', 'Droll', 'Dry',
                      'Earthy', 'Effeminate', 'Emotional', 'Enigmatic', 'Experimental', 'Familial', 'Folksy', 'Formal',
                      'Freewheeling', 'Frugal', 'Glamorous', 'Guileless', 'High-spirited', 'Huried', 'Hypnotic',
                      'Iconoclastic', 'Idiosyncratic', 'Impassive', 'Impersonal', 'Impressionable', 'Intense',
                      'Invisible', 'Irreligious', 'Irreverent', 'Maternal', 'Mellow', 'Modern', 'Moralistic',
                      'Mystical', 'Neutral', 'Noncommittal', 'Noncompetitive', 'Obedient', 'Old-fashined', 'Ordinary',
                      'Outspoken', 'Paternalistic', 'Physical', 'Placid', 'Political', 'Predictable', 'Preoccupied',
                      'Private', 'Progressive', 'Proud', 'Pure', 'Questioning', 'Quiet', 'Religious', 'Reserved',
                      'Restrained', 'Retiring', 'Sarcastic', 'Self-conscious', 'Sensual', 'Skeptical', 'Smooth', 'Soft',
                      'Solemn', 'Solitary', 'Stern', 'Stoiid', 'Strict', 'Stubborn', 'Stylish', 'Subjective',
                      'Surprising', 'Soft', 'Tough', 'Unaggressive', 'Unambitious', 'Unceremonious', 'Unchanging',
                      'Undemanding', 'Unfathomable', 'Unhurried', 'Uninhibited', 'Unpatriotic', 'Unpredicatable',
                      'Unreligious', 'Unsentimental', 'Whimsical']

    # 292
    negative_traits = ['Abrasive', 'Abrupt', 'Agonizing', 'Aimless', 'Airy', 'Aloof', 'Amoral', 'Angry', 'Anxious',
                       'Apathetic', 'Arbitrary', 'Argumentative', 'Arrogantt', 'Artificial', 'Asocial', 'Assertive',
                       'Astigmatic', 'Barbaric', 'Bewildered', 'Bizarre', 'Bland', 'Blunt', 'Biosterous', 'Brittle',
                       'Brutal', 'Calculating', 'Callous', 'Cantakerous', 'Careless', 'Cautious', 'Charmless',
                       'Childish', 'Clumsy', 'Coarse', 'Cold', 'Colorless', 'Complacent', 'Complaintive', 'Compulsive',
                       'Conceited', 'Condemnatory', 'Conformist', 'Confused', 'Contemptible', 'Conventional',
                       'Cowardly', 'Crafty', 'Crass', 'Crazy', 'Criminal', 'Critical', 'Crude', 'Cruel', 'Cynical',
                       'Decadent', 'Deceitful', 'Delicate', 'Demanding', 'Dependent', 'Desperate', 'Destructive',
                       'Devious', 'Difficult', 'Dirty', 'Disconcerting', 'Discontented', 'Discouraging', 'Discourteous',
                       'Dishonest', 'Disloyal', 'Disobedient', 'Disorderly', 'Disorganized', 'Disputatious',
                       'Disrespectful', 'Disruptive', 'Dissolute', 'Dissonant', 'Distractible', 'Disturbing',
                       'Dogmatic', 'Domineering', 'Dull', 'Easily Discouraged', 'Egocentric', 'Enervated', 'Envious',
                       'Erratic', 'Escapist', 'Excitable', 'Expedient', 'Extravagant', 'Extreme', 'Faithless', 'False',
                       'Fanatical', 'Fanciful', 'Fatalistic', 'Fawning', 'Fearful', 'Fickle', 'Fiery', 'Fixed',
                       'Flamboyant', 'Foolish', 'Forgetful', 'Fraudulent', 'Frightening', 'Frivolous', 'Gloomy',
                       'Graceless', 'Grand', 'Greedy', 'Grim', 'Gullible', 'Hateful', 'Haughty', 'Hedonistic',
                       'Hesitant', 'Hidebound', 'High-handed', 'Hostile', 'Ignorant', 'Imitative', 'Impatient',
                       'Impractical', 'Imprudent', 'Impulsive', 'Inconsiderate', 'Incurious', 'Indecisive', 'Indulgent',
                       'Inert', 'Inhibited', 'Insecure', 'Insensitive', 'Insincere', 'Insulting', 'Intolerant',
                       'Irascible', 'Irrational', 'Irresponsible', 'Irritable', 'Lazy', 'Libidinous', 'Loquacious',
                       'Malicious', 'Mannered', 'Mannerless', 'Mawkish', 'Mealymouthed', 'Mechanical', 'Meddlesome',
                       'Melancholic', 'Meretricious', 'Messy', 'Miserable', 'Miserly', 'Misguided', 'Mistaken',
                       'Money-minded', 'Monstrous', 'Moody', 'Morbid', 'Muddle-headed', 'Naive', 'Narcissistic',
                       'Narrow', 'Narrow-minded', 'Natty', 'Negativistic', 'Neglectful', 'Neurotic', 'Nihilistic',
                       'Obnoxious', 'Obsessive', 'Obvious', 'Odd', 'Offhand', 'One-dimensional', 'One-sided',
                       'Opinionated', 'Opportunistic', 'Oppressed', 'Outrageous', 'Overimaginative', 'Paranoid',
                       'Passive', 'Pedantic', 'Perverse', 'Petty', 'Pharissical', 'Phlegmatic', 'Plodding', 'Pompous',
                       'Possessive', 'Power-hungry', 'Predatory', 'Prejudiced', 'Presumptuous', 'Pretentious', 'Prim',
                       'Procrastinating', 'Profligate', 'Provocative', 'Pugnacious', 'Puritanical', 'Quirky',
                       'Reactionary', 'Reactive', 'Regimental', 'Regretful', 'Repentant', 'Repressed', 'Resentful',
                       'Ridiculous', 'Rigid', 'Ritualistic', 'Rowdy', 'Ruined', 'Sadistic', 'Sanctimonious', 'Scheming',
                       'Scornful', 'Secretive', 'Sedentary', 'Selfish', 'Self-indulgent', 'Shallow', 'Shortsighted',
                       'Shy', 'Silly', 'Single-minded', 'Sloppy', 'Slow', 'Sly', 'Small-thinking', 'Softheaded',
                       'Sordid', 'Steely', 'Stiff', 'Strong-willed', 'Stupid', 'Submissive', 'Superficial',
                       'Superstitious', 'Suspicious', 'Tactless', 'Tasteless', 'Tense', 'Thievish', 'Thoughtless',
                       'Timid', 'Transparent', 'Treacherous', 'Trendy', 'Troublesome', 'Unappreciative', 'Uncaring',
                       'Uncharitable', 'Unconvincing', 'Uncooperative', 'Uncreative', 'Uncritical', 'Unctuous',
                       'Undisciplined', 'Unfriendly', 'Ungrateful', 'Unhealthy', 'Unimaginative', 'Unimpressive',
                       'Unlovable', 'Unpolished', 'Unprincipled', 'Unrealistic', 'Unreflective', 'Unreliable',
                       'Unrestrained', 'Unself-critical', 'Unstable', 'Vacuous', 'Vague', 'Venal', 'Venomous',
                       'Vindictive', 'Vulnerable', 'Weak', 'Weak-willed', 'Well-meaning', 'Willful', 'Wishful', 'Zany']

    positve = list()
    neutral = list()
    negative = list()

    for i in range(options):
        positve.append(positive_traits[randrange(234)])
    print("Positve Traits:", positve)

    for i in range(options):
        neutral.append(neutral_traits[randrange(112)])
    print("Neutral Traits:", neutral)

    for i in range(options):
        negative.append(negative_traits[randrange(292)])
    print("Negative Traits:", negative)




# meant to roll all the dice you could need might be not super useful over all
def rolldice(d2, d3, d4, d5, d6, d8, d10, d12, d20, d100):
    total = 0

    if d2 > 0:
        d2l = list()
        for i in range(d2):
            d2l.append(randrange(2) + 1)
        print("D2 - ", end='')
        print(d2l)

    if d3 > 0:
        d3l = list()
        for i in range(d3):
            d3l.append(randrange(3) + 1)
        print("D3 - ", end='')
        print(d3l)

    if d4 > 0:
        d4l = list()
        for i in range(d4):
            d4l.append(randrange(4) + 1)
        print("D4 - ", end='')
        print(d4l)

    if d5 > 0:
        d5l = list()
        for i in range(d5):
            d5l.append(randrange(5) + 1)
        print("D5 - ", end='')
        print(d5l)

    if d6 > 0:
        d6l = list()
        for i in range(d6):
            d6l.append(randrange(6) + 1)
        print("D6 - ", end='')
        print(d6l)

    if d8 > 0:
        d8l = list()
        for i in range(d8):
            d8l.append(randrange(8) + 1)
        print("D8 - ", end='')
        print(d8l)

    if d10 > 0:
        d10l = list()
        for i in range(d10):
            d10l.append(randrange(10) + 1)
        print("D10 - ", end='')
        print(d10l)

    if d12 > 0:
        d12l = list()
        for i in range(d12):
            d12l.append(randrange(12) + 1)
        print("D12 - ", end='')
        print(d12l)

    if d20 > 0:
        d20l = list()
        for i in range(d20):
            d20l.append(randrange(20) + 1)
        print("D20 - ", end='')
        print(d20l)

    if d100 > 0:
        d100l = list()
        for i in range(d100):
            d100l.append(randrange(100) + 1)
        print("D100 - ", end='')
        print(d100l)


rolldice(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)