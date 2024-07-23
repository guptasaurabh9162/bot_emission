class EcoTrackBot:
    def __init__(self):
        # Define the main topics and their descriptions
        self.main_topics = {
            0: "Climate Change",
            1: "Carbon Footprint",
            2: "Pollution",
            3: "Renewable Energy",
            4: "Sustainability",
            5: "Carbon Emission Reduction",
            6: "Environmental Impact Assessment",
            7: "Climate Adaptation and Mitigation",
            8: "Education and Awareness",
            9: "Exit"
        }

        # Define the subtopics and their answers for each main topic
        self.subtopics = {
            0: {
                0: ("Global Warming", "Global warming refers to the long-term rise in Earth's average surface temperature due to human activities, especially the emission of greenhouse gases."),
                1: ("Greenhouse Gases", "Greenhouse gases trap heat in the atmosphere and include carbon dioxide, methane, nitrous oxide, and fluorinated gases."),
                2: ("Temperature Trends", "Temperature trends show the long-term changes in global temperatures, often depicted through graphs showing increasing temperatures over decades."),
                3: ("Extreme Weather Events", "Extreme weather events include phenomena such as hurricanes, heatwaves, droughts, and floods, which are becoming more frequent and severe due to climate change."),
                4: ("Ice Melt and Sea Level Rise", "Ice melt from glaciers and polar ice caps contributes to sea level rise, which poses risks to coastal communities and ecosystems."),
                5: ("Climate Policy and Agreements", "International agreements like the Paris Agreement aim to limit global warming and reduce greenhouse gas emissions."),
                6: ("Climate Change Impacts on Ecosystems", "Climate change affects ecosystems through changes in species distribution, habitat loss, and disruptions in ecological balance.")
            },
            1: {
                0: ("Personal Carbon Footprint", "A personal carbon footprint is the total amount of greenhouse gases emitted by an individual through activities such as driving, energy use, and consumption."),
                1: ("Corporate Carbon Footprint", "A corporate carbon footprint measures the total greenhouse gas emissions produced by a company, including operations, supply chains, and products."),
                2: ("Product Carbon Footprint", "The carbon footprint of a product includes emissions from raw material extraction, manufacturing, transportation, use, and disposal."),
                3: ("Carbon Offset Programs", "Carbon offset programs allow individuals and businesses to compensate for their emissions by investing in projects that reduce or absorb greenhouse gases elsewhere."),
                4: ("Carbon Footprint Calculation", "Carbon footprint calculation involves measuring the total emissions associated with activities or products using tools and methodologies like lifecycle assessment."),
                5: ("Reduction Strategies", "Strategies to reduce carbon footprint include improving energy efficiency, using renewable energy, reducing waste, and making sustainable choices."),
                6: ("Carbon Footprint and Lifestyle Choices", "Lifestyle choices such as diet, transportation, and energy use significantly impact one's carbon footprint, and changes can lead to reductions in emissions.")
            },
            2: {
                0: ("Air Pollution", "Air pollution is caused by emissions from vehicles, industrial processes, and other sources, leading to harmful effects on human health and the environment."),
                1: ("Water Pollution", "Water pollution results from contaminants such as chemicals, waste, and plastics entering water bodies, affecting aquatic life and water quality."),
                2: ("Soil Pollution", "Soil pollution occurs when harmful substances like pesticides, heavy metals, and industrial waste contaminate the soil, impacting plant growth and health."),
                3: ("Noise Pollution", "Noise pollution refers to excessive or harmful levels of noise from sources like traffic, industry, and construction, which can affect human health and wildlife.")
            },
            3: {
                0: ("Solar Energy", "Solar energy is harnessed from the sun's rays and converted into electricity or heat using technologies such as solar panels and solar thermal systems."),
                1: ("Wind Energy", "Wind energy is generated by converting the kinetic energy of wind into electricity using wind turbines."),
                2: ("Hydropower", "Hydropower generates electricity from the energy of flowing water, typically through dams or run-of-river systems."),
                3: ("Geothermal Energy", "Geothermal energy comes from the heat stored beneath the Earth's surface and can be used for electricity generation or direct heating applications."),
                4: ("Biomass Energy", "Biomass energy is produced from organic materials like wood, agricultural residues, and waste, and can be used for heating, electricity, and biofuels.")
            },
            4: {
                0: ("Sustainable Development Goals (SDGs)", "The SDGs are a set of 17 global goals adopted by the UN to address issues like poverty, inequality, and climate change, aiming for sustainable development."),
                1: ("Sustainable Agriculture", "Sustainable agriculture focuses on practices that maintain soil health, conserve water, reduce chemical use, and support biodiversity."),
                2: ("Green Building Practices", "Green building practices involve designing and constructing buildings with environmental considerations like energy efficiency, sustainable materials, and waste reduction."),
                3: ("Waste Reduction and Recycling", "Waste reduction and recycling aim to minimize waste generation and promote the reuse and recycling of materials to reduce environmental impact."),
                4: ("Sustainable Transportation", "Sustainable transportation includes methods that reduce environmental impact, such as public transit, cycling, electric vehicles, and efficient urban planning."),
                5: ("Sustainable Water Use", "Sustainable water use involves managing water resources to meet current needs without compromising future availability, including practices like water conservation and efficient usage."),
                6: ("Corporate Social Responsibility (CSR)", "CSR refers to businesses taking responsibility for their social, environmental, and economic impacts, often through initiatives that support sustainability and ethical practices.")
            },
            5: {
                0: ("Emission Reduction Strategies", "Emission reduction strategies include adopting cleaner technologies, improving energy efficiency, and transitioning to renewable energy sources."),
                1: ("Carbon Trading and Market Mechanisms", "Carbon trading involves buying and selling emission allowances as part of cap-and-trade systems, which aim to reduce overall emissions cost-effectively."),
                2: ("Renewable Energy Adoption", "Adopting renewable energy involves increasing the use of energy sources like solar, wind, and hydro, reducing reliance on fossil fuels."),
                3: ("Energy Efficiency Improvements", "Energy efficiency improvements focus on reducing energy consumption through better technology, practices, and behavior."),
                4: ("Carbon Capture and Storage (CCS)", "CCS involves capturing carbon dioxide emissions from sources like power plants and storing them underground to prevent them from entering the atmosphere."),
                5: ("Policy Measures and Regulations", "Policy measures and regulations are governmental actions to limit emissions, such as emission standards, carbon pricing, and incentives for green technologies.")
            },
            6: {
                0: ("Environmental Impact Statements (EIS)", "EIS are documents required by law to assess the potential environmental effects of proposed projects and to inform decision-making."),
                1: ("Risk Assessment and Management", "Risk assessment and management involve identifying, evaluating, and mitigating environmental risks to reduce potential negative impacts."),
                2: ("Mitigation Measures", "Mitigation measures are actions taken to reduce or eliminate adverse environmental impacts of projects or activities."),
                3: ("Environmental Monitoring", "Environmental monitoring involves systematically observing and measuring environmental parameters to track changes and ensure compliance with regulations.")
            },
            7: {
                0: ("Adaptation Strategies", "Adaptation strategies are actions taken to adjust to the impacts of climate change, such as building resilient infrastructure and changing agricultural practices."),
                1: ("Mitigation Technologies", "Mitigation technologies include innovations and practices aimed at reducing greenhouse gas emissions and enhancing carbon sequestration."),
                2: ("Community and Policy Responses", "Community and policy responses involve local and governmental actions to address and manage climate change impacts, such as public awareness campaigns and policy development.")
            },
            8: {
                0: ("Environmental Education Programs", "Environmental education programs aim to raise awareness and knowledge about environmental issues and promote sustainable practices."),
                1: ("Public Awareness Campaigns", "Public awareness campaigns seek to inform and engage the public on environmental issues through various media and activities."),
                2: ("Eco-friendly Practices and Lifestyle", "Eco-friendly practices and lifestyle involve adopting behaviors and choices that reduce environmental impact, such as reducing waste and conserving resources.")
            }
        }

    def display_main_topics(self):
        print("Select a main topic to learn more:")
        for key, value in self.main_topics.items():
            print(f"{key}: {value}")

    def display_subtopics(self, topic_id):
        print(f"\nSubtopics under '{self.main_topics[topic_id]}':")
        for key, value in self.subtopics.get(topic_id, {}).items():
            print(f"{key}: {value[0]}")

    def show_subtopic_info(self, main_topic_id, subtopic_id):
        subtopic_info = self.subtopics.get(main_topic_id, {}).get(subtopic_id, ("Subtopic not found.", "No information available."))
        return f"Information about '{subtopic_info[0]}': {subtopic_info[1]}"

    def start_chat(self):
        print("Welcome to EcoTrackBot!")
        name = input("What is your name? ").strip()
        print(f"Hello, {name}! How can I assist you today?")

        while True:
            self.display_main_topics()
            try:
                main_selection = int(input("Enter the number corresponding to the main topic you want to learn about: "))
                if main_selection == 9:
                    print("Goodbye!")
                    break
                if main_selection not in self.main_topics:
                    print("Invalid selection. Please choose a valid main topic.")
                    continue

                self.display_subtopics(main_selection)
                try:
                    sub_selection = int(input("Enter the number corresponding to the subtopic you want to learn about: "))
                    if sub_selection not in self.subtopics.get(main_selection, {}):
                        print("Invalid selection. Please choose a valid subtopic.")
                        continue

                    response = self.show_subtopic_info(main_selection, sub_selection)
                    print(response)

                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            more_queries = input("Do you have more queries? (yes/no): ").strip().lower()
            if more_queries == 'no':
                print("Goodbye!")
                break

if __name__ == "__main__":
    bot = EcoTrackBot()
    bot.start_chat()