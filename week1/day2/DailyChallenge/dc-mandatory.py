# Challenge 1 - Letter Index Dictionary
# Ask the user for a word and create a dictionary of character indices.
word = input("Please enter a word: ")
letter_indices = {}
for index, character in enumerate(word):
    if character in letter_indices:
        letter_indices[character].append(index)
    else:
        letter_indices[character] = [index]
print(letter_indices)


# Challenge 2 - Affordable Items
# Create a list of items that can be purchased with the wallet amount.
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}
wallet = input("Please enter the wallet amount (for example $300): ")
clean_wallet = int(wallet.replace("$", "").replace(",", ""))

basket = []
for item, price in items_purchase.items():
    item_price = int(price.replace("$", "").replace(",", ""))
    if item_price <= clean_wallet:
        basket.append(item)
        clean_wallet -= item_price

if basket:
    print(sorted(basket))
else:
    print("Nothing")
