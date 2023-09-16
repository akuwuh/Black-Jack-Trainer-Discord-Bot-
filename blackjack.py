import nextcord
import random
from nextcord.ui import Button, View
from PIL import Image, ImageDraw, ImageColor, ImageFont
from io import BytesIO

card_width = 138
card_height = 210

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

# no aces or pairs
hard_totals = {
    #IND: 0   1   2   3   4   5   6   7   8   9
    #DC:  2   3   4   5   6   7   8   9   10  A
    8: ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],  # and below
    9: ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],
    10: ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"],
    11: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
    12: ["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"],
    13: ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
    14: ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
    15: ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
    16: ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
    17: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"]  # and above
}

# A + __
soft_totals = {
    #IND: 0   1   2   3   4   5   6   7   8   9
    #DC:  2   3   4   5   6   7   8   9   10  A
    2: ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],
    3: ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],
    4: ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
    5: ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
    6: ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],
    #    2    3    4    5    6    7   8   9   10  A
    7: ["Ds", "Ds", "Ds", "Ds", "Ds", "S", "S", "H", "H", "H"],
    #    2   3   4   5   6    7   8   9   10  A
    8: ["S", "S", "S", "S", "Ds", "S", "S", "S", "S", "S"],
    9: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"]
}

pairs = {
    #IND: 0   1   2   3   4   5   6   7   8   9
    #DC:  2   3   4   5   6   7   8   9   10  A
    11: ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],  #Aces
    2: ["Yn", "Yn", "Y", "Y", "Y", "Y", "N", "N", "N", "N"],
    3: ["Yn", "Yn", "Y", "Y", "Y", "Y", "N", "N", "N", "N"],
    4: ["N", "N", "N", "Yn", "Yn", "N", "N", "N", "N", "N"],
    5: ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    6: ["Yn", "Y", "Y", "Y", "Y", "N", "N", "N", "N", "N"],
    7: ["Y", "Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N"],
    8: ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
    9: ["Y", "Y", "Y", "Y", "Y", "N", "Y", "Y", "N", "N"],
    10: ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N"]
}

answer_conv = {
    "H": "Hit",
    "S": "Stand",
    "D": "Double",
    "Ds": "Double/Stand",
    "Y": "Split",
    "Yn": "Split if DAS"
}

# suits = ["S","D","C","H"]

# draw_deck = ["AD", "AC", "AH", "AS", "2D", "2C", "2H",
#                 "2S", "3D", "3C", "3H", "3S",
#                 "4D", "4C", "4H", "4S", "5D", "5C", "5H",
#                 "5S", "6D", "6C", "6H", "6S",
#                 "7D", "7C", "7H", "7S", "8D", "8C", "8H",
#                 "8S", "9D", "9C", "9H", "9S",
#                 "10D", "10C", "10H",
#                 "10S", "JD", "JC", "JH", "JS", "QD", "QC",
#                 "QH", "QS",
#                 "KD", "KC", "KH", "KS"]

# class Cards:
#     def __init__(self, cards, dealer=False): #takes in list of cards
#         self.cards = cards #list
#         self.dealer = dealer

#     def display(self):
#         num_cards = len(self.cards)

#         maxWidth = (int(card_width/ 3) * (num_cards - 1)) + card_width + 20

#         HAND = Image.new("RGB", (maxWidth, card_height + 40))
#         DRAW = ImageDraw.Draw(HAND)

#         font = ImageFont.truetype('calibri.ttf', size=24)

#         for i in self.cards:
#             card_suit = random.choice(suits)
#             link = "deck/" + i + card_suit + ".png"
#             card = Image.open(link)
#             card = card.resize((card_width, card_height))

#             HAND.paste(card, (10 + int(card_width / 3) * i, 10))
#             DRAW.text((30 + int(card_width / 3) * i, card_height + 15), str(i), fill=ImageColor.getrgb("#ffffff"), font=font)

#         with BytesIO() as img:
#             HAND.save(img, 'PNG')
#             img.seek(0)
#             filename = 'hand.png'
#             if self.dealer == True:
#                 filename = 'dealer.png'
#             file = nextcord.File(fp=img, filename='dealer.png')
#             return file


class Game:

  def __init__(self, interaction):
    #private
    self.interaction = interaction
    self.is_pair = False
    self.card1 = None
    self.card1_val = None
    self.card2 = None
    self.card2_val = None
    self.dealer = None
    self.dealer_val = None

  def button_view(self):

    view = View()

    hit = Button(label="Hit!", style=nextcord.ButtonStyle.primary)
    stand = Button(label="Stand", style=nextcord.ButtonStyle.primary)
    double = Button(label="Double/Hit", style=nextcord.ButtonStyle.primary)
    double_stand = Button(label="Double/Stand",
                          style=nextcord.ButtonStyle.primary)
    split = Button(label="Split", style=nextcord.ButtonStyle.primary)
    split_das = Button(label="Split (DAS only)",
                       style=nextcord.ButtonStyle.primary)

    async def play_again_callback(interaction: nextcord.Interaction):
      game_instance = Game(interaction)  # Create a new game instance
      original_message = interaction.message
      await original_message.delete()
      await game_instance.generate_game()  # Start a new game

    async def end_game_callback(interaction: nextcord.Interaction):
      original_message = interaction.message
      await original_message.delete()

    async def update_embed(message, interaction):
      # Get the original message to edit (no need for .fetch() in this case)
      original_message = interaction.message

      new_embed = embed = nextcord.Embed(colour=nextcord.Colour.purple())
      new_embed.set_thumbnail(
          url=
          "https://png.pngtree.com/png-vector/20220812/ourmid/pngtree-blackjack-png-image_6107450.png"
      )

      new_embed.description = message

      play_again_button = nextcord.ui.Button(
          style=nextcord.ButtonStyle.primary,
          label="Play Again",
          custom_id="play_again")
      end_game_button = nextcord.ui.Button(style=nextcord.ButtonStyle.danger,
                                           label="End Game",
                                           custom_id="end_game")

      new_view = nextcord.ui.View()

      play_again_button.callback = play_again_callback
      end_game_button.callback = end_game_callback
      new_view.add_item(play_again_button)
      new_view.add_item(end_game_button)

      await original_message.delete()
      await self.interaction.send(embed=new_embed, view=new_view)

    async def button_callback_hit(interaction: nextcord.Interaction):
      tup = self.eval("H")  # (true/false, answer)
      message = ""
      if tup[0]:  # right
        message = "**Correct! ✅**"
      else:
        message = "**Wrong! ❌**\nAnswer: " + "**" + tup[1] + "**"
      await update_embed(message, interaction)

    async def button_callback_stand(interaction: nextcord.Interaction):
      tup = self.eval("S")  # (true/false, answer)
      message = ""
      if tup[0]:  # right
        message = "**Correct! ✅**"
      else:
        message = "**Wrong! ❌**\nAnswer: " + "**" + tup[1] + "**"
      await update_embed(message, interaction)

    async def button_callback_double(interaction: nextcord.Interaction):
      tup = self.eval("D")  # (true/false, answer)
      message = ""
      if tup[0]:  # right
        message = "**Correct! ✅**"
      else:
        message = "**Wrong! ❌**\nAnswer: " + "**" + tup[1] + "**"
      await update_embed(message, interaction)

    async def button_callback_double_stand(interaction: nextcord.Interaction):
      tup = self.eval("Ds")  # (true/false, answer)
      message = ""
      if tup[0]:  # right
        message = "**Correct! ✅**"
      else:
        message = "**Wrong! ❌**\nAnswer: " + "**" + tup[1] + "**"
      await update_embed(message, interaction)

    async def button_callback_split(interaction: nextcord.Interaction):
      tup = self.eval("Y")  # (true/false, answer)
      message = ""
      if tup[0]:  # right
        message = "**Correct! ✅**"
      else:
        message = "**Wrong! ❌**\nAnswer: " + "**" + tup[1] + "**"
      await update_embed(message, interaction)

    async def button_callback_split_das(interaction: nextcord.Interaction):
      tup = self.eval("Yn")  # (true/false, answer)
      message = ""

      if tup[0]:  # right
        message = "**Correct! ✅**"
      else:
        message = "**Wrong! ❌**\nAnswer: " + "**" + tup[1] + "**"

      await update_embed(message, interaction)

    # Set the callback functions for the buttons
    hit.callback = button_callback_hit
    stand.callback = button_callback_stand
    double.callback = button_callback_double
    double_stand.callback = button_callback_double_stand
    split.callback = button_callback_split
    split_das.callback = button_callback_split_das

    view.add_item(hit)
    view.add_item(stand)
    view.add_item(double)
    view.add_item(double_stand)

    if self.is_pair == True:
      view.add_item(split)
      view.add_item(split_das)
    return view

  def eval(self, action):  # this is so hard

    def eval_soft(non_ace_val, dealer_ind):
      ans = soft_totals[non_ace_val][dealer_ind]
      return (ans == action, answer_conv[ans])

    def eval_hard(total, dealer_ind):
      if total < 8: total = 8
      if total > 17: total = 17
      ans = hard_totals[total][dealer_ind]
      return (ans == action, answer_conv[ans])

    if self.is_pair and not (pairs[self.card1_val][self.dealer_val - 2] == "N"
                             and action != "Y"
                             and action != "Yn"):  # keep evaluating
      return (pairs[self.card1_val][self.dealer_val - 2] == action,
              answer_conv[pairs[self.card1_val][self.dealer_val - 2]])

    if max(self.card1_val, self.card2_val) == 11:  # soft total
      return eval_soft(min(self.card1_val, self.card2_val),
                       self.dealer_val - 2)
    else:  # hard total
      return eval_hard(self.card1_val + self.card2_val, self.dealer_val - 2)

  async def generate_game(self):

    self.card1 = self.generate_card()
    self.card2 = self.generate_card()
    self.dealer = self.generate_card(dealer_card=True)
    self.card1_val = self.card1[1]
    self.card2_val = self.card2[1]
    self.dealer_val = self.dealer[1]

    if self.card1 == self.card2:  # checks if we are playing pairs
      self.is_pair = True

    embed = self.generate_game_embed()
    view = self.button_view()
    await self.interaction.send(embed=embed, view=view)

  def reg_card_visual(self, card):
    suit_symbols = ['♠', '♦', '♥', '♣']
    suit = random.choice(suit_symbols)
    if len(card) == 1: card += " "
    return "```" + "\n" + " " "\n" + card + " " + suit + "\n" + " " + "\n" + "```"

  def generate_game_embed(self):
    embed = nextcord.Embed(colour=nextcord.Colour.purple())

    c1_visuals = self.reg_card_visual(self.card1[0])
    c2_visuals = self.reg_card_visual(self.card2[0])
    d_visuals = self.reg_card_visual(self.dealer[0])

    #embed.title = "Your cards: \n" + self.card1[0] + " " + self.card2[0] + "\n" + "Dealer Upcard: \n" + self.dealer[0]
    embed.set_thumbnail(
        url=
        "https://png.pngtree.com/png-vector/20220812/ourmid/pngtree-blackjack-png-image_6107450.png"
    )

    embed.description = "**Hand:**"
    embed.add_field(name="", value=c1_visuals)

    embed.add_field(name="", value=c2_visuals)
    embed.add_field(name="", value="")

    embed.add_field(
        name="Dealer:",
        value=d_visuals,
    )

    embed.add_field(name="", value="")

    embed.add_field(name="", value="")
    embed.title = "\n"
    embed.set_footer(text="Choose your answer:")
    embed.set_author(name="")

    return embed

  def generate_card(self, dealer_card=False):
    if self.card1 != None and self.card1[
        0] == "A" and dealer_card == False:  # if first card is ace, dont give jqk
      random_card = random.choice(list(
          cards.keys())[0:9])  # removed ace (first element)
    elif self.card1 != None and (
        self.card1[0] == "J" or self.card1[0] == "Q" or self.card1[0] == "K"
        or self.card1[0] == "10"
    ) and dealer_card == False:  # if first card is jqk, dont give ace
      random_card = random.choice(list(
          cards.keys())[1:])  # removed last 3 element(jqk)
    else:
      random_card = random.choice(list(
          cards.keys()))  # else just do it normally
    return (random_card, cards[random_card])  # display and val
