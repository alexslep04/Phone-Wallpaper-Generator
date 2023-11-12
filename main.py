# have it only generate one new prompt but make it generate it 3 times
# I need to make some type of memory storage system

import openai
import requests

openai.api_key = ''


class promptlist:
    def __init__(self, maxsize):
        self.size = maxsize
        self.list = []

    def put(self, value):
        self.list.append(value)
        if len(self.list) > self.size:
            self.list.pop(0)

    push = append = put

    def pop(self):
        if len(self.list) != 0:
            return self.list.pop(0)

    get = pop

    def toString(self, seperator=' '):
        return seperator.join(self.list)

    join = getString = toString


prompts = promptlist(maxsize=5)
aiAction = """The following prompts are used to create portrait images. They all have certain similarities and
            differences. Identify these commonalities and disparities. Then, based on the similarities, create one
           new prompt for images, incorporating unique elements to mirror the differences in the original prompts.
           Your response should only consist of the new prompt. I do not want to see the analysis of what you
           were looking for. Ensure and say that the portrait is vertically oriented. Ensure that the raccoon
           is an ordinary raccoon and is not directly taking part of whatever mystical thing is occurring. 
           Do not make it underwater"""

prompts.put("""Design a vertically oriented digital scene with portrait dimensions of w=3885xh=1792. Amidst the vast 
            desert dunes lies a once-great city, its ruins barely visible under the shifting sands. Crystal obelisks 
            rise, casting a soft, magical luminescence. The night sky is filled with twinkling stars. A singular raccoon
            , unadorned and in its natural state, looks up from its vantage point on a ruined wall, simply observing. 
            Nearby, a human paladin, not resembling any animals and in shining armor, holds aloft a sword that gleams 
            with an otherworldly glow. This scene should evoke a sense of awe, blending the mysteries of the past 
            with the wonders of the unknown.""")

prompts.put("Create a vertically oriented watercolor painting in the dimensions of 3885x1792, capturing a serene "
            "mountain valley during the twilight hours. Steep cliffs embrace a hidden valley, where ancient temples "
            "stand,overgrown with moss and vines. A waterfall cascades from a high peak, creating a sparkling pond "
            "below. In the midst of this scene, a singular raccoon, in its natural state without adornments, sits by "
            "the water's edge, simply observing. Nearby, a human archer with no animalistic features, and with a quiver"
            " full of glowing arrows, prepares to aim at a distant, ethereal target. The entire setting should be "
            "filled with the ambiance of enchantment, mixing natural beauty and magical elements.")

prompts.put("Design a vertical digital scene with dimensions of 3885x1792, creating a vertically oriented depiction of "
            "a post-apocalyptic cityscape. Ruins of skyscrapers, now entwined with nature's reclaiming vines and moss, "
            "reach upwards. At the city's core is a vibrant oasis, with clear waters reflecting the juxtaposition of "
            "nature and decay. Around this pond, survivors have crafted shelters from salvaged materials, with gardens "
            "flourishing amidst the ruins. Within this scene of renewal, a single raccoon, appearing as it would in "
            "nature, drinks peacefully from the oasis, providing a touch of wild amidst the remnants of civilization. "
            "The image should encapsulate both the melancholy of lost times and the resilient spirit of life.")

prompts.put("Craft a vertical digital artwork in the dimensions of 3885x1792, which emphasizes a vertically oriented "
            "scene of a magical forest library. Towering ancient trees with sprawling roots create natural wooden "
            "shelves filled with multicolored, softly glowing books. Between the trees, bioluminescent plants emit a "
            "gentle illumination, and the air is thick with magical particles. Faeries with luminous wings flit between"
            " the shelves, deeply engrossed in the texts. In the foreground, amidst this wonder, a singular raccoon, "
            "without any adornments, curiously observes the library's activities, standing out as a natural element ")

prompts.put("Develop a vertical acrylic canvas painting sized 3885x1792 illustrating a majestic celestial body seen "
            "through the roof of a derelict observatory. Shattered glass panes allow the vivid hues of space; twinkling"
            " stars, swirling galaxies and distant planets, to pierce through into the dilapidated interior. A singular"
            " raccoon, ordinary and with no adornments, perches atop the broken telescope, staring curiously towards "
            "the cosmic display. Nearby, a cloaked astronomer stands, holding aloft an ethereal staff. This image "
            "should blend the theme of interstellar fascination with the melancholy of forgotten knowledge.")


def set_new_prompt():
    return prompts


print(prompts.list)
newInput = prompts.join(seperator="\n\n")
print("\n\n" + newInput)


def main():
    while True:
        print(prompts.list[0])  # Fixed index access error
        chat_response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {openai.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4",
                "messages": [{"role": "user", "content": aiAction + newInput}]
            }
        )
        response = chat_response.json()['choices'][0]['message']['content']
        print(response)

        question1 = input("do you approve of this prompt? (y/n): ")
        if question1 == 'y':
            prompts.put(response)
        question2 = input("do you want to generate a new prompt? (y/n): ")
        if question2 == 'y':
            continue
        else:
            exit()


if __name__ == "__main__":
    main()  # Ensures main function is called when script is run
