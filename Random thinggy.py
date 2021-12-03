import random

# Location Variables #

Location1 = "South Island, New Zealand! New Zealand's South Island brims with majestic landscapes at every turn, from dramatic mountains to fjords to glaciers. Here, you can admire the mountains of Fiordland National Park, a UNESCO World Heritage Site, from hiking trails or a boat on Milford Sound. At night, journey to the University of Canterbury's Mount John Observatory to gaze at the starry skies. You can also indulge your inner daredevil in Queenstown, explore two of the most accessible glaciers in the world on the island's west coast or sample delicious food and wine in the Marlborough region."
Location2 = "Paris! The magnetic City of Light draws visitors from around the globe who come to see iconic attractions like the Eiffel Tower, the Louvre and the Arc de Triomphe. But what travelers really fall in love with are the city's quaint cafes, vibrant markets, trendy shopping districts and unmistakable je ne sais quoi charm. Get lost wandering along Paris' cobblestone streets, or grab a croissant and relax on the banks of the Seine for hours. If you're up for a quick daytrip, head about 15 miles southwest of the city center to another must-see attraction: the Palace of Versailles."
Location3 = "Bora Bora! What this small French Polynesian island may lack in size it makes up for in sheer tropical beauty. Here, you'll find picturesque beaches, lush jungles and luxurious resorts. The island's dormant volcano, Mount Otemanu, makes for a great photo-op or challenging hike, and the friendly Bora Bora locals can help you catch a glimpse of the island's best sights during an off-road excursion. To relax, head to Matira Beach for crystal-clear water and soft sand. Although a trip to Bora Bora is very expensive, most travelers say it's worth every penny."
Location4 = "Maui! Whether you're driving along the Road to Hana, enjoying a bird's-eye view of the lush coastline from a helicopter, snorkeling with sea turtles or simply relaxing on the Hawaiian island's honey- or black-colored beaches, you'll find that Maui is unlike any other tropical destination. Don't miss a chance to visit Haleakala National Park, which is home to the world's largest dormant volcano. You should also attend a luau for a dose of local culture and a taste of Hawaiian specialties like poi, poke and mahimahi."
Location5 = "Tahiti! Travel to this island – the largest in French Polynesia – if you've been dreaming of a vacation spent lazing in a lavish overwater bungalow. Beyond the posh resorts, Tahiti boasts black sand beaches, a bustling capital and prime snorkeling and surfing conditions. If you're looking for more cultural experiences, check out some of the island's ancient temples or shop at its traditional covered markets. To save money, opt to stay in a vacation rental."
Location6 = "London! London is a world unto itself. The eclectic neighborhoods, which are home to a blend of historical landmarks and modern-day attractions, can keep you occupied for days. If it's your first time in London, plan to visit the Tower of London, Tate Modern, Buckingham Palace or the British Museum before sitting down to a classic afternoon tea. The best time to travel to London is during the warmer months, but be warned that this is also the busiest and most expensive time of year."
Location7 = "Rome! When you visit the Eternal City, prepare to cross a few must-see attractions – including the Colosseum, the Trevi Fountain and the Pantheon – off of your bucket list. Additional treasures, such as St. Peter's Basilica and the Sistine Chapel, can be found in nearby Vatican City. Escape the tourist crowds by taking a twilight stroll along the cobblestone streets of Trastevere, or head to Mercato Centrale Roma to sample local delicacies like gelato and pizza. Before leaving, peruse some of Rome's lesser-known museums, art galleries and boutiques."
Location8 = "Phuket! When you visit the Eternal City, prepare to cross a few must-see attractions – including the Colosseum, the Trevi Fountain and the Pantheon – off of your bucket list. Additional treasures, such as St. Peter's Basilica and the Sistine Chapel, can be found in nearby Vatican City. Escape the tourist crowds by taking a twilight stroll along the cobblestone streets of Trastevere, or head to Mercato Centrale Roma to sample local delicacies like gelato and pizza. Before leaving, peruse some of Rome's lesser-known museums, art galleries and boutiques."
Location9 =  "Tokyo! Simply setting foot in Japan's cosmopolitan capital is an experience within itself. A city known for its bustling streets and flashing neon signs, Tokyo has an electric energy and plenty of attractions to discover. Foodies won't be let down by the city's fresh sushi and hearty ramen. Budding photographers and adrenaline junkies will love taking in the sweeping panoramas from the top of the Tokyo Skytree. Shopaholics will find plenty of must-have designer products in Ginza. And for history buffs, Tokyo offers centuries-old temples and shrines to explore"
Location10 = "Maldives! It is not cheap or easy to reach, but this isolated paradise between the Arabian and Laccadive seas is the personification of a dreamy tropical vacation. In this South Asian destination, which is made up of more than 1,000 islands, thatched-roof bungalows sit above crystal-clear aquamarine waters, providing easy water access and a romantic atmosphere. Fill your days with beach trips, spa treatments and snorkeling or scuba diving excursions. If cabin fever sets in, pay a visit to the capital, Malé, where you'll find historic mosques and open-air markets!"


# Actual question to determine Location # 


name = input("Enter your name: ")
input(name + ", The great beautiful AI will provide you the answer to a question you may not know you had! We will give you the best place to vacation and some facts about it! ")

choice = random.randint(1,10)

if choice == 1:
    answer = Location1
elif choice == 2:
    answer = Location2
elif choice == 3:
    answer = Location3  
elif choice == 4:
    answer = Location4
elif choice == 5:
    answer = Location5
elif choice == 6:
    answer = Location6
elif choice == 7:
    answer = Location7
elif choice == 8:
    answer = Location8
elif choice == 9:
    answer = Location9
else:
    answer = Location10


    # Final Print #

print("The magical AI has determined that you should vacation to", answer)
