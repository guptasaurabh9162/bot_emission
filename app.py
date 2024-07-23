from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class EcoTrackBot:
    def __init__(self):
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
        self.subtopics = {
            0: {  # Climate Change
                0: ("Global Warming", "Global warming refers to the long-term rise in Earth's average surface temperature due to human activities."),
                1: ("Greenhouse Gases", "Greenhouse gases trap heat in the atmosphere and include carbon dioxide, methane, nitrous oxide, and fluorinated gases."),
                # Add more subtopics for Climate Change
            },
            1: {  # Carbon Footprint
                0: ("Definition", "A carbon footprint is the total amount of greenhouse gases emitted by an individual, organization, event, or product, expressed as carbon dioxide equivalent."),
                1: ("How to Reduce", "To reduce your carbon footprint, consider using renewable energy sources, enhancing energy efficiency, reducing waste, and adopting sustainable practices."),
                # Add more subtopics for Carbon Footprint
            },
            2: {  # Pollution
                0: ("Air Pollution", "Air pollution is the presence of harmful substances in the atmosphere, primarily caused by emissions from vehicles, industries, and agricultural activities."),
                1: ("Water Pollution", "Water pollution is the contamination of water bodies, such as rivers, lakes, and oceans, often caused by industrial discharge and improper waste disposal."),
                # Add more subtopics for Pollution
            },
            3: {  # Renewable Energy
                0: ("Solar Energy", "Solar energy is harnessed from the sun's rays and can be converted into electricity or heat."),
                1: ("Wind Energy", "Wind energy is captured from wind currents using wind turbines to generate electricity."),
                # Add more subtopics for Renewable Energy
            },
            4: {  # Sustainability
                0: ("Definition", "Sustainability is the practice of meeting current needs without compromising the ability of future generations to meet their own needs."),
                1: ("How to Practice", "You can practice sustainability by reducing waste, conserving energy, using sustainable products, and supporting eco-friendly businesses."),
                # Add more subtopics for Sustainability
            },
            5: {  # Carbon Emission Reduction
                0: ("Techniques", "Techniques for reducing carbon emissions include improving energy efficiency, using renewable energy sources, and adopting low-carbon technologies."),
                1: ("Policies", "Policies to reduce carbon emissions include carbon pricing, emission trading systems, and regulatory standards."),
                # Add more subtopics for Carbon Emission Reduction
            },
            6: {  # Environmental Impact Assessment
                0: ("Purpose", "Environmental Impact Assessment (EIA) is a process to evaluate the environmental effects of a proposed project before it is carried out."),
                1: ("Steps", "The steps in EIA typically include screening, scoping, impact assessment, and reporting."),
                # Add more subtopics for Environmental Impact Assessment
            },
            7: {  # Climate Adaptation and Mitigation
                0: ("Adaptation", "Climate adaptation involves making adjustments to natural or human systems to minimize the negative impacts of climate change."),
                1: ("Mitigation", "Climate mitigation involves efforts to reduce or prevent the emission of greenhouse gases."),
                # Add more subtopics for Climate Adaptation and Mitigation
            },
            8: {  # Education and Awareness
                0: ("Importance", "Education and awareness about environmental issues help people understand the impacts and encourage sustainable practices."),
                1: ("Methods", "Methods of raising awareness include public campaigns, educational programs, and community involvement."),
                # Add more subtopics for Education and Awareness
            },
            9: {  # Exit
                0: ("Exit", "Thank you for using EcoTrackBot. Have a great day!"),
                # No additional subtopics
            }
        }

    def get_main_topics(self):
        return self.main_topics

    def get_subtopics(self, topic_id):
        return self.subtopics.get(topic_id, {})

    def get_subtopic_info(self, main_topic_id, subtopic_id):
        subtopic_info = self.subtopics.get(main_topic_id, {}).get(subtopic_id, ("Subtopic not found.", "No information available."))
        return subtopic_info

bot = EcoTrackBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_main_topics')
def get_main_topics():
    topics = bot.get_main_topics()
    return jsonify(topics)

@app.route('/get_subtopics/<int:main_topic_id>')
def get_subtopics(main_topic_id):
    subtopics = bot.get_subtopics(main_topic_id)
    return jsonify(subtopics)

@app.route('/get_subtopic_info/<int:main_topic_id>/<int:subtopic_id>')
def get_subtopic_info(main_topic_id, subtopic_id):
    subtopic_info = bot.get_subtopic_info(main_topic_id, subtopic_id)
    return jsonify({'title': subtopic_info[0], 'info': subtopic_info[1]})

if __name__ == '__main__':
    app.run(debug=False,host=0.0.0.0)