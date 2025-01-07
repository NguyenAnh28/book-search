import spacy
import csv

nlp = spacy.load('en_core_web_lg')

descriptions = [
    "A young boy discovers he has magical powers in a hidden world, where he must battle dark forces to protect his friends and defeat an ancient evil threatening both worlds.",
    "In a dystopian future, society is divided into strict social classes. One girl dares to defy the system, sparking a revolution that could change everything, but at a great personal cost.",
    "A group of astronauts journey to a distant planet to investigate a strange anomaly. What they find will challenge their understanding of life, space, and their own humanity.",
    "A young detective unravels a web of mystery and intrigue in a small town, where no one is who they seem. The case pushes him to his limits, testing his intelligence and morals.",
    "In a world where technology controls everything, one rebel hacker seeks to expose the truth. As she digs deeper, she uncovers secrets that could destroy everything she knows.",
    "A young woman discovers an old journal containing mysterious instructions. As she follows them, she begins to uncover long-forgotten family secrets that change her life forever.",
    "A group of survivors in a post-apocalyptic world must navigate through harsh conditions, facing both human and environmental threats. Trust and survival are their only weapons in a shattered world.",
    "Set during the Civil War, this epic novel follows a soldier's journey as he battles both external enemies and his own internal struggles, questioning the cost of war and the meaning of loyalty.",
    "An ambitious scientist discovers a way to reverse aging. But his discovery comes with unforeseen consequences, and he must grapple with moral dilemmas that could alter the course of history.",
    "A lonely artist living in a small town starts receiving mysterious letters from an anonymous admirer. The correspondence leads to a surprising and life-changing revelation.",
    "In an ancient civilization, a young scholar discovers a prophecy that foretells the end of the world. She embarks on a dangerous quest to prevent the prophecy from becoming reality.",
    "A once-wealthy family loses everything in a financial crisis. The story follows their struggle to survive, rebuild their lives, and rediscover what truly matters in the face of adversity.",
    "A detective and his partner race against time to catch a serial killer who leaves cryptic clues at each crime scene. The case becomes personal as the killer taunts them, testing their resolve.",
    "A young prince must navigate a treacherous court full of intrigue and betrayal to claim his rightful place on the throne. Along the way, he learns harsh lessons about power, loyalty, and sacrifice.",
    "In a city ruled by corrupt politicians, an idealistic journalist uncovers a conspiracy that could change the course of history. The danger escalates as she becomes a target for those in power.",
    "A soldier returns home after a long deployment, only to find that his small town has changed in ways he never expected. As he adjusts to civilian life, he uncovers long-hidden secrets from his past.",
    "A young girl is trapped in a time loop, reliving the same day over and over. As she struggles to break free, she discovers that the key to escaping lies within her own choices and actions.",
    "An old man tells the story of his life, full of adventure, heartbreak, and triumph. His memories take him on a journey through time, as he reflects on the moments that shaped who he became.",
    "A woman’s life is turned upside down when she receives a letter from her estranged mother, inviting her to a family reunion. The journey forces her to confront her past and come to terms with old wounds.",
    "In a world where dreams can be manipulated, a group of dream hunters must navigate a dangerous landscape to capture elusive dreams for wealthy clients. But one hunter has plans of her own.",
    "A young couple moves to a remote village, where they uncover strange occurrences and secrets that the townspeople are desperate to keep hidden. They must decide whether to flee or uncover the truth."
]

description_vectors_list = []

for description in descriptions:
    doc = nlp(description)
    
    # Reduce the vector to the first 128 elements
    reduced_vector = doc.vector[:128].tolist()

    entry = {"vector": reduced_vector, "description": description}
    description_vectors_list.append(entry)

# Writing to CSV
with open('dummy_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['description', 'vector']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for entry in description_vectors_list:
        writer.writerow({'description': entry['description'], 'vector': str(entry['vector'])})

print("CSV file created: dummy_data.csv")
