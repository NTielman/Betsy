from models import create_tables
from queries import create_user, add_product_to_catalog, add_images_to_product, add_product_tags

##################################### users ##############################################
# possible to use any of these user details to log in, or create your own account

yuki = {
    "full_name": 'Yukine Masashi',
    "username": 'Yukiyuki_UwU',
    "password": 'BTSistheBest',
    "address": 'San Fransokyo 1234',
    "bio": "Hi i'm yuki, i'm 23 and i love crafting cute things. If you're into kawaii culture, unicorns, and love pink you're going to love my handcrafted goodies. Have a look at my shop, you won't regret it. Nyaaa :3",
    "avatar_url": '../static/images/yuki.jpg'
}

sam = {
    "full_name": 'Samantha Addams',
    "username": 'TheAddamsFamily',
    "password": 'sam.dams26',
    "address": 'The middle of nowhere 43',
    "bio": "Love relaxing at home with a good spell book, and deck of tarot cards. I'm a moon child and believe in the power of mysticism. Also love indulging into my more creepy fascinations every so often. If you like what you see, consider adding my store to your ghouly favorite list ",
    "avatar_url": '../static/images/sam.jpg'
}

alaska = {
    "full_name": 'Alaska Jones',
    "username": 'The.Lion.Queen',
    "password": 'RickIsA-Morty',
    "address": 'Brooklyntown 168',
    "bio": "Hey, welcome to my profile. I'm more of a collector of vintage items, than a creator. Though sometimes i enjoy making jewelry in my free time. I especially love crafting with gems and crystals. If you're into that sort of thing, you may want to keep an occasional eye on this profile ;)",
    "avatar_url": '../static/images/aska.jpg'
}


##################################### products ##############################################
# possible to edit, modify and update any of these products, or create your own

unicorn = {
    'title': 'Unicorn Plush Toy Handmade',
    'description': 'A soft sweet and cute friend to love and to hold at night when watching thriller movies',
    'price_in_cents': 542,
    'qty': 8,
    'vendor': yuki,
    'tags': ['unicorn', 'cute', 'sleep'],
    'images': ['https://ae01.alicdn.com/kf/H693039e8a0f64224863dc772ec383e50H.jpg?width=1000&height=1000&hash=2000', 'https://ae01.alicdn.com/kf/H52f5a8a2e4d041d7a70dbeb170859e233.jpg?width=1000&height=1000&hash=2000', 'https://ae01.alicdn.com/kf/Hc274bc43d49c49dbb197c4a2f4bf79dbq.jpg?width=1000&height=1000&hash=2000', 'https://ae01.alicdn.com/kf/He6cc8bc8600549b398e2dd83627233815.jpg?width=1000&height=1000&hash=2000', 'https://ae01.alicdn.com/kf/H5e311a0c5e7a4753acaef10948a913d1O.jpg?width=1000&height=1000&hash=2000']
}

avocado_keychain = {
    'title': 'Cute Avocado Keychain Hanger',
    'description': "Not only are they fruity and healthy, now they'll also help you find your keys in the cutest manner possible. these advocado hangers are handmade from resin.",
    'price_in_cents': 129,
    'qty': 14,
    'vendor': yuki,
    'tags': ['avocado', 'cute', 'keychain'],
    'images': ['https://ae01.alicdn.com/kf/HTB14zY9U4naK1RjSZFBq6AW7VXa8.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/HTB1PhjOU7PoK1RjSZKbq6x1IXXae.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/HTB1X8LAU3TqK1RjSZPhq6xfOFXaB.jpg?width=800&height=800&hash=1600']
}

cat_ears = {
    'title': 'Cat ears With Bell Cosplay Hair Accessory',
    'description': "Cats rule the world and now so can you! With these fluffy cotton cat eared hairbands you'll have all eyes on you",
    'price_in_cents': 581,
    'qty': 23,
    'vendor': yuki,
    'tags': ['cat', 'hair', 'cosplay'],
    'images': ['https://ae01.alicdn.com/kf/H91c5968f2ff747e7b699de81e58295e8y.jpg?width=1600&height=1600&hash=3200', 'https://ae01.alicdn.com/kf/Hbeaec5896a8b422fb6d83245ab38394fF.jpg?width=1600&height=1600&hash=3200', 'https://ae01.alicdn.com/kf/Hc1a7acec867d4857afd579698ad3e06dD.jpg?width=1600&height=1600&hash=3200', 'https://ae01.alicdn.com/kf/Hbeb38d14895a4bd7839335e11590d9bep.jpg?width=1600&height=1600&hash=3200']
}

earrings = {
    'title': 'Candy Earrings Cute and Funny Eaaring Gifts',
    'description': "These miniature food eaarings are not only cute to look at they were handcrafted using epoch resin and food coloring. These cute accessories look good enough to eat, and will make your style absolutely flavorful",
    'price_in_cents': 381,
    'qty': 5,
    'vendor': yuki,
    'tags': ['earrings', 'cute', 'candy', 'lolipop'],
    'images': ['https://ae01.alicdn.com/kf/H19ff8bc035d04d789ea5354c5b7a7cce0.jpg', 'https://ae01.alicdn.com/kf/Hbf0d8e3e71b14e12b9c255b3e36365f15.jpg', 'https://ae01.alicdn.com/kf/H4d11e7eb58394ab1a3f5285b2e546fe3h.jpg', 'https://ae01.alicdn.com/kf/H804d808811c64c548bd0b7963578490aA.jpg'
               ]
}

plush_bacpack = {
    'title': 'Bear Backpack Comfy Back To School',
    'description': "Oh my cuteness, is that a bear on your back? Not only is this soft cotton plushy bag un-dear-ably cute to look at, it's also spacious enough inside to carry your books and laptop with. ",
    'price_in_cents': 1793,
    'qty': 7,
    'vendor': yuki,
    'tags': ['bag', 'kawaii', 'pink'],
    'images': ['https://ae01.alicdn.com/kf/H3a50d08ae4b44f409839045c6a862feb9.jpg', 'https://ae01.alicdn.com/kf/H0b405fe77bfd4f3a91be5fe369965fadK.jpg', 'https://ae01.alicdn.com/kf/H34f47f54400e47799f70a625462833bcA.jpg', 'https://ae01.alicdn.com/kf/Haf899a3278824a02a2dfc05e659dabb4R.jpg'
               ]
}

sailor_skirt = {
    'title': 'Sailor Skirt Plaid Pink Skirt Harajuku',
    'description': "short and sexy, or sweet and kawaii? This soft pastel colored skirt is made from stretchy soft materials, making for a comfortable fit for any occassion ",
    'price_in_cents': 3751,
    'qty': 32,
    'vendor': yuki,
    'tags': ['skirt', 'plaid', 'sexy'],
    'images': ['https://ae01.alicdn.com/kf/H28642efccd7b4c528db48f343cf5f41dZ.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/H22a847b39597447abec0f9ef546ca4acE.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/H2b5ccd84a3a947b98c7220f426117f35s.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/Hffe6dba22f9a479bb9f9a0d283c77bbbi.jpg?width=800&height=800&hash=1600']
}

cosplay_wig = {
    'title': 'Cosplay Purple Pink Wig Sakura Erza Raven',
    'description': "A gorgeously colored purple and pink wig for your cosplaying neeeds. made with synthetic hair, that can withstand heat up to 250 degrees. It's durable versatile and a great addition for any cosplayer to have",
    'price_in_cents': 2080,
    'qty': 16,
    'vendor': yuki,
    'tags': ['cosplay', 'purple', 'wig', 'pink'],
    'images': ['https://ae01.alicdn.com/kf/H0e9161fcb26d48bdb224843227572d580.jpg']
}

harajuku_socks = {
    'title': 'Cute and Colorful Harajuku socks Printed',
    'description': "Ttired of waring borin' ol' socks? M too, that's why i made thee handknitted harajuku socks with various cute and funny designs to pick from. your boring sock days are over.",
    'price_in_cents': 211,
    'qty': 32,
    'vendor': yuki,
    'tags': ['socks', 'comfy', 'funny'],
    'images': ['https://ae01.alicdn.com/kf/H1e1ef8bcfc904d3aa13a451d7726bde89.jpg', 'https://ae01.alicdn.com/kf/H8cef2f52b7f44157bf238556e2770c12L.jpg', 'https://ae01.alicdn.com/kf/H53d839f7d685458bb72b066c3cfe1b99N.jpg', 'https://ae01.alicdn.com/kf/H3d2dbabe08c7447e81855f168e7bf8c2f.jpg']
}

totoro = {
    'title': 'Totoro Toy Plush Gifts',
    'description': "Who doesn't love a Miyazaki film. Now you can be reminded of your cuddly favorite character wherever you go with this Totoro toy figurine.",
    'price_in_cents': 262,
    'qty': 42,
    'vendor': yuki,
    'tags': ['totoro', 'cute'],
    'images': ['https://ae01.alicdn.com/kf/Ha6f592c439a14cf585d4232a7fb6616cy.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/Hf93067e9ba1e498696a736049051b26cd.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/Hb3ea5ae0a96542cbac6ebbecc34339555.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/H9505ec431e214d678d04cccd50f11bb3O.jpg?width=800&height=800&hash=1600']
}

garter_belt = {
    'title': 'Sexy Garter Belt Harness Set',
    'description': "For the wilder days. Made from faux leather, the materials are stretchy, comfortable and form-fitting",
    'price_in_cents': 1546,
    'qty': 22,
    'vendor': sam,
    'tags': ['sexy', 'garter', 'harness'],
    'images': ['https://ae01.alicdn.com/kf/HTB1qLiQev1G3KVjSZFkq6yK4XXar.jpg', 'https://ae01.alicdn.com/kf/HTB1XKmVeBKw3KVjSZFOq6yrDVXaF.jpg', 'https://ae01.alicdn.com/kf/HTB1ueaSeBaE3KVjSZLeq6xsSFXaK.jpg']
}

spiked_boots = {
    'title': 'Spiky Goth Boots Platform',
    'description': "Don't these gorgeous boots just make you want to try putting them in someone's face? I'm not saying they were made to kick people with, but ... i mean with all that spiky goodness they make it tempting tho",
    'price_in_cents': 9800,
    'qty': 45,
    'vendor': sam,
    'tags': ['boots', 'spikes', 'comfy'],
    'images': ['https://ae01.alicdn.com/kf/H542f2c6beadc46b4b74004c3b415dddcg.jpg?width=757&height=655&hash=1412', 'https://ae01.alicdn.com/kf/He3afb4d216054071b713d0f83df1a77fS.jpg?width=670&height=919&hash=1589', 'https://ae01.alicdn.com/kf/H5c5fac2fb63e41fdbcfe1c9b9b660532j.jpg?width=750&height=1200&hash=1950', 'https://ae01.alicdn.com/kf/H11085947b7234c6090cdb797ee582d06j.jpg?width=750&height=1200&hash=1950']
}

choker = {
    'title': 'Cute Choker',
    'description': "What can i say i got my days when i'm suddenly into cute stuff. if you love the sweet kitten or the sexy cougar look, try on one of my leather chokers.",
    'price_in_cents': 3670,
    'qty': 17,
    'vendor': sam,
    'tags': ['choker', 'cute', 'necklace'],
    'images': ['https://ae01.alicdn.com/kf/H28cd729cb1a2446bb70cfd9f8b9ba4c7n.jpg?width=1000&height=1000&hash=2000', 'https://ae01.alicdn.com/kf/H9489845b3bf8416d8da9bba9c2382c596.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/H6dd9aa9603cc48b9bc84cca818b5fe77L.jpg?width=800&height=800&hash=1600']
}

shades = {
    'title': 'Slim Shadies Sexy Black Shades',
    'description': "All true vampires need protection from the sun in every way possible. Try on one of my self-made chiller designs",
    'price_in_cents': 4570,
    'qty': 13,
    'vendor': sam,
    'tags': ['shades', 'sunglasses'],
    'images': ['https://ae01.alicdn.com/kf/H811b7725e14748008de142fc640b05c7R.jpg', 'https://ae01.alicdn.com/kf/H268493ea62e6417b8aa77bce187b7d7dv.jpg', 'https://ae01.alicdn.com/kf/Ha9df103c95f94846b2777e459e05b1baq.jpg']
}

skull = {
    'title': 'Skull Set Decor Home',
    'description': "You can never have enough skulls laying around your house.",
    'price_in_cents': 3740,
    'qty': 5,
    'vendor': sam,
    'tags': [],
    'images': ['https://ae01.alicdn.com/kf/Hf79f45f50866438ba71f0065dfa9ec7eX.jpg', 'https://ae01.alicdn.com/kf/H8ef8c778de9b487fb8801d34b031d425W.jpg', 'https://ae01.alicdn.com/kf/Haa7f180b0eb747efb097215c20f12ec2C.jpg']
}

goth_skirt = {
    'title': 'Goth ailor Skirt Cute Harajuku',
    'description': "Most goth gals have an inner 'cutesy' side. With these black and pink skirts, you won't have to decide between your two personalitiess anymore. Unleash your inner baby monster.",
    'price_in_cents': 2045,
    'qty': 58,
    'vendor': sam,
    'tags': ['kawaii', 'cute', 'skirt', 'comfy'],
    'images': ['https://ae01.alicdn.com/kf/H2fe8f6a3232340e1a36f7ea5d7f0617bE.jpg', 'https://ae01.alicdn.com/kf/H70755b14366a41c49acbeb9a91ee6548y.jpg', 'https://ae01.alicdn.com/kf/Hcf0fc10510954c75a48223fd012110a4l.jpg', 'https://ae01.alicdn.com/kf/H33905f3ee94e4acf83cabb798765f7c3b.jpg']
}

scented_candles = {
    'title': 'Scented Candles Halloween Autumn Relaxing',
    'description': "These candles come in 3 scented variations: Pumpkin Spice, Autumn Night, and Smokey Musk. If you're as into halloween season ass i am, these candles will be sure to bring the spooky spirits in",
    'price_in_cents': 300,
    'qty': 60,
    'vendor': sam,
    'tags': ['relax', 'candles', 'sleep'],
    'images': ['https://ae01.alicdn.com/kf/Hd0261bf77e134a0098d0d7995af3a6b1c.jpg?width=750&height=1275&hash=2025', 'https://ae01.alicdn.com/kf/H28ca80cd5555403f918363dd5a3d6de2u.jpg?width=750&height=1275&hash=2025', 'https://ae01.alicdn.com/kf/H241948339e5e41d9af523a5a6d89c5e7O.jpg?width=750&height=1274&hash=2024', 'https://ae01.alicdn.com/kf/H241948339e5e41d9af523a5a6d89c5e7O.jpg?width=750&height=1274&hash=2024', 'https://ae01.alicdn.com/kf/Hd89fcbd72b8f41cc898146ee8f210eb9D.jpg?width=750&height=1275&hash=2025']
}

bath_bomb = {
    'title': 'Glitter Bath Bomb',
    'description': "Creates a beautiful glittery explosion and relseases relaxing aromas. I use these to wind down after a stressfull week",
    'price_in_cents': 600,
    'qty': 50,
    'vendor': alaska,
    'tags': ['relax', 'bath', 'pink'],
    'images': ['https://ae01.alicdn.com/kf/H56325c2497da4e6f9f956661f51dc288b.jpg', 'https://ae01.alicdn.com/kf/Hfaf1d9919a0047af8d181ec004888e0ag.jpg', 'https://ae01.alicdn.com/kf/H06dc40fc03404d68a4fb9b056efec9f9N.jpg']
}

crystal_gem = {
    'title': 'Crystal Gems Jewelry',
    'description': "They say Gems and Crystal have magical healing powers. If your interrested to know which gem to choose based on your birthsign, contact me. These are great as gifts to loved ones",
    'price_in_cents': 1560,
    'qty': 20,
    'vendor': alaska,
    'tags': ['necklace', 'crystals', 'handmade'],
    'images': ['https://ae01.alicdn.com/kf/H36ba6a1e2c4f4014a12a5737c612fdc56.jpg', 'https://ae01.alicdn.com/kf/H18d1de464f1340889ef62e6b3a3392baw.jpg', 'https://ae01.alicdn.com/kf/H33df8a92ed0149f29beed69904d3d3baZ.jpg']
}

bracelet = {
    'title': 'Hand made Silver Bracelet',
    'description': "Made of sterling silver, and all natural products",
    'price_in_cents': 2500,
    'qty': 15,
    'vendor': alaska,
    'tags': ['jewelry'],
    'images': ['https://ae01.alicdn.com/kf/Ha494879551ec40669a7023b91cbc53015.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/H46e6cce9ec77425a8b9ee4e43dabd347L.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/Ha97c111c0a434b87ae7252d7d055a953y.jpg?width=500&height=500&hash=1000', 'https://ae01.alicdn.com/kf/H681ee31baa004ec8bb2295da2cdee588l.jpg?width=800&height=800&hash=1600']
}

cacti_plant = {
    'title': 'Small Cacti Plant',
    'description': "I started growing these late last summer, and oh' my how they've bloomed. I have about 15 of them now in the house. I'm very proud of how well they've grown. Included in the packlage will be a guide on how to take further care of your cactus baby",
    'price_in_cents': 300,
    'qty': 12,
    'vendor': alaska,
    'tags': ['plant', 'botanic', 'cacti', 'garden', 'cute'],
    'images': ['https://ae01.alicdn.com/kf/HTB1udsOXxD1gK0jSZFyq6AiOVXau.jpg', 'https://ae01.alicdn.com/kf/Hba8013795e6d444f9105285d83932bdeU.jpg', 'https://ae01.alicdn.com/kf/HTB1UbwIXq67gK0jSZFHq6y9jVXa8.jpg', 'https://ae01.alicdn.com/kf/H42cd2add7e514b18991c0d2bae99e283Q.jpg']
}

jewelry = {
    'title': 'Costum Made Jewelry',
    'description': "In my free time i combine gems and metals to create one of a kind jewelry pieces. If you'd like me to make one for you just send me your custom measurements along with a description of what you're looking for and i can make you an offer",
    'price_in_cents': 1750,
    'qty': 100,
    'vendor': alaska,
    'tags': ['jewelry'],
    'images': ['https://ae01.alicdn.com/kf/H31b289e56e534a77bb7a2195aa79f13ez.jpg', 'https://ae01.alicdn.com/kf/H63a96460ce8742aea12356686e1e6981b.jpg', 'https://ae01.alicdn.com/kf/H8a728a548c9e4bc69936ffbdd06084870.jpg', 'https://ae01.alicdn.com/kf/Hb2ab0d7868e540f78a408eb3a74d1ef6T.jpg', 'https://ae01.alicdn.com/kf/H32bd46fb8da64ad0b8ef0aac84f8ec4bt.jpg']
}

phonecase = {
    'title': 'Pretty Phonecase',
    'description': "In a crafty mood again. I made a batch of 20 phonecases all with cute different designs. See any you like? Or have an idea for a phone case of your own, just shoot me a message",
    'price_in_cents': 345,
    'qty': 18,
    'vendor': alaska,
    'tags': ['phonecase', 'cute', 'crafts'],
    'images': ['https://ae01.alicdn.com/kf/HTB1HNbnBkCWBuNjy0Faq6xUlXXaM.jpg', 'https://ae01.alicdn.com/kf/HTB1QF6UBhGYBuNjy0Fnq6x5lpXa6.jpg', 'https://ae01.alicdn.com/kf/HTB1f5AwjHsrBKNjSZFpq6AXhFXah.jpg', 'https://ae01.alicdn.com/kf/HTB1yxfnBkCWBuNjy0Faq6xUlXXab.jpg?width=1080&height=1618&hash=2698']
}

make_up_brush = {
    'title': 'Magical Girl Make Up Brush Set',
    'description': "Not your average make up brush sets. These come in different designs from mermaid, to unicorn, to fairies, you name it!",
    'price_in_cents': 750,
    'qty': 4,
    'vendor': alaska,
    'tags': ['unicorn', 'cute', 'magic'],
    'images': ['https://ae01.alicdn.com/kf/H7d6554c930b54b73b2c66685c7cefb25o.jpg?width=1920&height=1920&hash=3840', 'https://ae01.alicdn.com/kf/H7892ca1040ad46da824202f13e105a9eb.jpg?width=1920&height=1920&hash=3840', 'https://ae01.alicdn.com/kf/H18ddcdb04acf41819eb3605cb723188aN.jpg?width=1920&height=1920&hash=3840', 'https://ae01.alicdn.com/kf/H745f3374fcac423591a450590df8a3bc8.jpg?width=1920&height=1920&hash=3840']
}

##################################### functions ##############################################
yuki_products = [unicorn, avocado_keychain, cat_ears, earrings,
                 plush_bacpack, sailor_skirt, cosplay_wig, harajuku_socks, totoro]
sam_products = [garter_belt, spiked_boots, choker,
                shades, skull, goth_skirt, scented_candles]
alaska_products = [bath_bomb, crystal_gem, bracelet,
                   cacti_plant, jewelry, phonecase, make_up_brush]

betsy_users = [yuki, sam, alaska]
user_products = [yuki_products, sam_products, alaska_products]


def create_users(users):
    for user in users:
        create_user(user_name=user['username'], user_full_name=user['full_name'], user_address=user['address'],
                    user_bio=user['bio'], user_avatar=user['avatar_url'], user_password=user['password'])


def create_products(product_list):
    for products in product_list:
        for product in products:
            prod_id = add_product_to_catalog(product)
            if prod_id:
                tag_list = product['tags']
                add_product_tags(prod_id, tag_list)
                image_list = product['images']
                add_images_to_product(prod_id, image_list)


def create_fake_db_accounts():
    '''creates 3 users with around 10 products each 
    for testing site functionality with'''
    create_tables()
    create_users(betsy_users)
    create_products(user_products)
