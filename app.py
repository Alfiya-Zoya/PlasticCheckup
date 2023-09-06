import streamlit as st
import time
from PIL import Image as PILImage
from PIL import Image
import tensorflow as tf
import numpy as np
import pymongo
st.set_page_config(page_title = "My Webpage",page_icon=":♻:",layout="wide")
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["cognizant"]
s_c = db["Seller"]
r_c = db["Buyer"]
a=db["Admin"]
b=db["Sell_details"]
c=db["Buy_details"]
def save_to_mongodb(data):
    b.insert_one(data)
def save_to_mongod(data):
    c.insert_one(data)
# Function to register a new user with a type (NGO or Recycling Companies)
def register_user(username, email, password, user_type):
    user_data = {
        "username": username,
        "email": email,
        "password": password,
    }
    if user_type == "Seller":
        s_c.insert_one(user_data)
    elif user_type == "Buyer":
        r_c.insert_one(user_data)

# Streamlit app
def register():
    with st.sidebar:
        st.title("Dashboard")
        if st.button("Register"):
            st.session_state.page = "register"
            st.experimental_rerun()
        if st.button("Login"):
            st.session_state.page = "login"
            st.experimental_rerun()
        if st.button("About Us"):
            st.session_state.page = "about"
            st.experimental_rerun()
        if st.button("Contact Us"):
            st.session_state.page = "contact"
            st.experimental_rerun()
    st.title("Registration Page")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    user_type = st.selectbox("Select User Type", ["Buyer", "Seller"])

    if st.button("Submit"):
        # Register the user
        register_user(username, email, password, user_type)
        st.success("Registration successful!")
        st.session_state.page = "details"
def details():
    st.title("Plastic Order Form")
    company_name = st.text_input("Company Name")
    address = st.text_area("Address")
    contract_no = st.text_input("Contract Number")
    user_type = st.selectbox("Select User Type", ["Buyer", "Seller"])
    
    confirm = st.button("Confirm")
    if confirm: 
        if user_type == "Seller":
            order_data = {
                "company_name": company_name,
                "address": address,
                "contract_no": contract_no,
            }
            save_to_mongodb(order_data)
        elif user_type == "Buyer":
            order_data = {
                "company_name": company_name,
                "address": address,
                "contract_no": contract_no,
            }
            save_to_mongod(order_data)
        st.button("Exit")
        if exit:
            st.session_state.page="mainpage"
            #st.experimental_rerun()

def selling():
    with st.sidebar:
        st.title("Dashboard")
        if st.button("Prices"):
            st.session_state.page = "price"
            st.experimental_rerun()
        if st.button("Purchase"):
            st.session_state.page = "purchase"
            st.experimental_rerun()
    st.image('BANNER.jpg', caption='Photo 1', use_column_width=True)

def price():
    with st.sidebar:
        st.title("Dashboard")
        if st.button("Prices"):
            st.session_state.page = "price"
            st.experimental_rerun()
        if st.button("Purchase"):
            st.session_state.page = "purchase"
            st.experimental_rerun()
    products = [
        {
            "name": "PET Plastic",
            "description": "Polyethylene terephthalate, also called PET, is the name of a type of clear, strong, lightweight and 100% recyclable plastic. Unlike other types of plastic, PET plastic is not single-use -- it is 100% recyclable, versatile, and made to be remade.",
            "price": "Rs.75000 per metric ton",
            "image_url": "https://d2cbg94ubxgsnp.cloudfront.net/Pictures/2000xAny/4/9/1/108491_pet_shutterstock_95088004.jpg",
            
        },
        {
            "name": "HDPE Plastic",
            "description": "High Density Polyethylene is a polyethylene thermoplastic made from petroleum. HDPE is commonly recycled and made into composite wood or plastic lumber. HDPE is a Type 2 plastic commonly used in making containers for milk, motor oil, shampoos and conditioners, soap bottles, detergents, and bleaches.",
            "price": "Rs.90000 per metric ton",
            "image_url": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6bKKbGwndtm2J6Z8NEjR30w_snSpM7Bjc02pMMa8RZ6zsSa36ZnjCIM5yxkFEFlt8bSzRS4AaRXbBKpvNHSI750-QKkFXsiCkrb_B56cyXa5FVPqmgv76aEPnlKUCc7y8XUxyKwJRmX8jFBhwQicJfMPqHRV84deD1LxdBP6kwu1r4GMWTDwRb3Pq/w455-h305/HDPE%202023.jpg",
            
        },
        {
            "name": "PVC Plastic",
            "description": "Polyvinyl Chloride (PVC or Vinyl) is a high-strength thermoplastic material. It is widely used in applications such as pipes, medical devices, and wire & cable insulation...the list is endless. It is the world's third-most widely produced synthetic plastic polymer.",
            "price": "Rs.70000 per metric ton",
            "image_url": "https://d1whtlypfis84e.cloudfront.net/guides/wp-content/uploads/2019/08/30123706/PVC-Plastic-1024x683.jpg",
            
        },
            
        {
            "name": "LDPE Plastic",
            "description": "Low density polyethylene, commonly shortened to LDPE, is a type of polyethylene defined by a density range of 917–930 kg/m3 . It is resistant to impact, moisture and offers good chemical resistance.",
            "price": "Rs.80000 per metric ton",
            "image_url": "https://4.imimg.com/data4/PJ/MK/MY-11619405/ldpe-plastic-bag-500x500.jpg",
            
        },
        {
            "name": "PP Plastic",
            "description": "Given its inherent flexibility, PP can be recycled back into many different products, including clothing fibers, industrial fibres, food containers, dishware etc.",
            "price": "Rs.85000 per metric ton",
            "image_url": "https://europlas.com.vn/Data/Sites/1/media/pp/polypropylene-plastic-is-a-common-material.jpg",
        },
        {
            "name": "PS Plastic",
            "description": "Polystyrene (PS) is available in various grades and qualities to suit numerous uses. While virgin PS is commonly used for packaging, electronics, building, and construction as well as medical applications, recycled PS is used in building and construction.",
            "price": "Rs.82000 per metric ton",
            "image_url": "https://www.chemicalsafetyfacts.org/wp-content/uploads/shutterstock_1027804891-scaled-1.jpg",
        },
        {
            "name": "Other Plastic",
            "description": "Recycled plastics are used to create all sorts of items, such as packaging, bags, car components, furniture, building materials, paint pots and even kerbstones.",
            "price": "Rs.95000 per metric ton",
            "image_url": "https://concept-stories.s3.ap-south-1.amazonaws.com/test/Stories%20-%20Images_story_121243/image_2020-08-27%2009%3A49%3A38.447752%2B00%3A00",
        },
        
        
    ]

    # Title and introduction
    st.title("Products Available")
    st.write("Explore some amazing products below:")

    # Display products
    for product in products:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(product["image_url"], use_column_width=True)
        with col2:
            st.write(f"**{product['name']}**")
            st.write(product["description"])
            st.write(f"Price: {product['price']}")
def plastic():
    st.title("Plastic Input")

    # Input fields
    plastic_quantity = st.number_input("Quantity of Plastic (in tons)", min_value=0, step=1)
    uploaded_image = st.file_uploader("Upload an Image of the Plastic", type=["jpg", "jpeg", "png"])
    
    form_submitted = False  # Initialize form_submitted as False

    if st.button("Submit"):
        form_submitted = True 
        # Save the submitted data to variables
        st.write(f"Plastic Quantity: {plastic_quantity} kg")
        
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_column_width=True)
        else:
            st.write("No image uploaded.")
        total_price = plastic_quantity * 40000
        st.success(f"Total Price: Rs.{total_price:.2f}")
        st.write("Order Accepted Successfully")

    # Display the "Exit" button only if the form has been submitted
    if form_submitted:
        st.button("Exit")
        if exit:
            st.session_state.page = "mainpage"  # Set the session_state variable to navigate back to "mainpage"


def about():
    with st.sidebar:
        st.title("Dashboard")
        if st.button("Register"):
            st.session_state.page = "register"
            st.experimental_rerun()
        if st.button("Login"):
            st.session_state.page = "login"
            st.experimental_rerun()
        if st.button("About Us"):
            st.session_state.page = "about"
            st.experimental_rerun()
        if st.button("Contact Us"):
            st.session_state.page = "contact"
            st.experimental_rerun()
    st.title("ABOUT US")
    st.write("At PLASTIC CHECKUP, we're on a quest to transform how we manage plastic waste in order to have a long-lasting influence on the environment. We set out on our adventure with a strong enthusiasm for sustainability and a determination to address the problem of excessive plastic consumption. We have worked tirelessly in collaboration with NGOs and local groups to collect plastic debris in an ethical manner. However, we didn't just stop at collection. We have faith in the capability of change. Our project's core is the complex science of plastic categorization. Our skill in categorising plastics into separate groups—from PET to PVC, PS to PC, HDPE to LDPE, and PP—has been refined over time. We make sure that each type of plastic reaches the highest standards through innovative techniques and strict quality control.")
    st.write("#")
    st.write("Our goal is to establish a circular economy where plastics are reborn, repurposed, and recreated. Our vision goes beyond recycling. We work with progressive businesses to connect them with the precise plastics they require to lessen their environmental impact and promote a greener society. We at [Your Project Name] are more than just a team; we are a group of people united by a common goal. To promote sustainability, protect the environment, and reimagine the use of plastics in the future, we are environmental stewards, educators, and inventors. Rewrite the history of plastics with us as we embark on this momentous path. Together, we can stop the spread of plastic waste and create a world where recycling is a way of life rather than just a choice.")
def contact():
    with st.sidebar:
        st.title("Dashboard")
        if st.button("Register"):
            st.session_state.page = "register"
            st.experimental_rerun()
        if st.button("Login"):
            st.session_state.page = "login"
            st.experimental_rerun()
        if st.button("About Us"):
            st.session_state.page = "about"
            st.experimental_rerun()
        if st.button("Contact Us"):
            st.session_state.page = "contact"
            st.experimental_rerun()
    st.title("CONTACT US")
    st.write("#")

    st.write("If you have any questions or need assistance, please feel free to contact our team:")


    with st.container():

        left, mid, right = st.columns(3)

        profile = {
            "image": "profile.webp",
        }

        with left:
            st.image(profile["image"], caption='XXX', use_column_width=True)
            st.write("email: xxx@gmail.com")
            st.write("phone: +1 (123) 456-7890")
        with mid:
            st.image(profile["image"], caption='YYY', use_column_width=True)
            st.write("email: yyy@gmail.com")
            st.write("phone: +1 (123) 456-7890")


        with right:
            st.image(profile["image"], caption='ZZZ', use_column_width=True)
            st.write("email: zzz@gmail.com")
            st.write("phone: +1 (123) 456-7890")


def main_page():
    st.title("Welcome to the PlasticCheckup")
    with st.sidebar:
        st.title("Dashboard")
        if st.button("Register", key="register_button"):
            st.session_state.page = "register"
            st.experimental_rerun()
        if st.button("Login", key="login_button"):
            st.session_state.page = "login"
            st.experimental_rerun()
        if st.button("About Us", key="about_button"):
            st.session_state.page = "about"
            st.experimental_rerun()
        if st.button("Contact Us", key="contact_button"):
            st.session_state.page = "contact"
            st.experimental_rerun()
    images = ['https://theaffordableorganicstore.com/wp-content/uploads/2022/11/TAOS-blogs-4-1024x512.jpg.webp','https://newsmobile.in/wp-content/uploads/2017/04/20132F042F222F082Fearthdaynai.28961.jpg',
            'https://www.rts.com/wp-content/uploads/2020/10/shutterstock_1345281257_opt.jpg']
    image_placeholder = st.empty()
    while(True):
        for i in range(len(images)):
            image_placeholder.image(images[i], use_column_width=True, caption=f"Image {i+1}")
            time.sleep(3)

def login():
    with st.sidebar:
        st.title("Dashboard")
        if st.button("Register"):
            st.session_state.page = "register"
            st.experimental_rerun()
        if st.button("Login"):
            st.session_state.page = "login"
            st.experimental_rerun()
        if st.button("About Us"):
            st.session_state.page = "about"
            st.experimental_rerun()
        if st.button("Contact Us"):
            st.session_state.page = "contact"
            st.experimental_rerun()
    st.title("Login Page")
    name = st.text_input("Enter Username")
    email = st.text_input("Enter User ID")
    ipass = st.text_input("Enter password", type="password")
    submit = st.button("Log-in")

    if submit:
        row = db["Seller"].find_one({"email": email})
        if not row:
            row1 = db["Buyer"].find_one({"email": email})
            if not row1:
                row2 = db["Admin"].find_one({"email":email})
                if not row2:
                    st.write("Wrong Credentials! Please try again!")
                    return
                else:
                    pass2 = row2["password"]
                    if str(pass2) == ipass:
                        st.write("ADMIN LOGIN SUCCESSFUL")
                        st.session_state.page="upload"
                    else:
                        st.write("Wrong Credentials! Please try again!!")
            else:
                pass1 = row1["password"]
                if str(pass1) == ipass:
                    st.write("BUYER LOGIN SUCCESSFUL")
                    st.session_state.page="selling"
                else:
                    st.write("Wrong Credentials! Please try again!!!")
        else:
            pass0 = row["password"]
            if str(pass0)==ipass:
                st.write("SELLER LOGIN SUCCESSFUL")
                st.session_state.page="plastic"
            else:
                st.write("Wrong Credentials! Please try again!!!!")

# Load the trained model
model_path = "model.h5"
model = tf.keras.models.load_model(model_path)
def preprocess_image(image):
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    return np.expand_dims(image_array, axis=0)
def upload():
           
    st.title("Plastic Classification App")
    st.write("Upload an image to classify the type of plastic")
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        preprocessed_image = preprocess_image(image)
        prediction = model.predict(preprocessed_image)
        predicted_class = np.argmax(prediction)
        class_labels = ["HDPE", "LDPE", "OTHERS", "PET", "PP", "PS", "PVC"]
        type=class_labels[predicted_class]
        st.write(f"**Predicted Class: {class_labels[predicted_class]}**")
        if type == 'HDPE':
                info_data = [
                    {
                        "Company": "KW Plastics and Merlin Plastics",
                        "Description": "Recycle HDPE into high-quality resin for various applications.",
                        "Email": "https://www.kwplastics.com/contact-us/"
                    },
                    {
                        "Company": "JM Eagle",
                        "Description": "Leading manufacturer that incorporates recycled HDPE into its pipe production.",
                        "Email": "contactjm@jmeagle.com"
                    },
                    {
                        "Company": "Trex and Advanced Environmental Recycling Technologies (AERT)",
                        "Description": "Produce composite lumber made from recycled HDPE for outdoor furniture, decking, fencing, and construction applications.",
                        "Email": "recycle@trex.com"
                    },
                    {
                        "Company": "Jindal Plastic Industries",
                        "Description": "Based in Delhi, known for its plastic recycling services, including HDPE recycling.",
                        "Contact Number": "080 4155 4473"
                    },
                    {
                        "Company": "Panchal Plastic Machinery Pvt. Ltd.",
                        "Description": "Specializes in the manufacturing of plastic recycling machinery and offers solutions for HDPE recycling.",
                        "Contact Number": "+91 70464 63391"
                    }
                ]
                st.title("HDPE Recycling Companies Information")
                st.write("High-Density Polyethylene (HDPE) is a versatile and widely used type of plastic known for its durability, strength, and resistance to various environmental factors. HDPE is a versatile plastic used in various applications, including packaging, pipes, toys, and household items. It has high strength and durability, making it suitable for products that require impact resistance, such as bottles for cleaning agents, milk jugs, and shampoo bottles. HDPE is more opaque than PET and is available in a variety of colours. It has excellent chemical resistance and is often used for storing chemicals, detergents, and other potentially reactive substances.")
                st.table(info_data)
        elif type == 'LDPE':
                info_data = [
                    {
                        "Company": "Trex, Advanced Environmental Recycling Technologies (AERT), Novolex",
                        "Description": "Involved in recycling LDPE for flexible packaging films and bags.",
                        "Contact Number": "(800) 845-6051"
                    },
                    {
                        "Company": "Tangent Technologies and Bedford Technology",
                        "Description": "Specialize in producing composite lumber made from recycled LDPE for outdoor decking, fencing, and construction applications.",
                        "Contact Number": "099003 06000"
                    },
                    {
                        "Company": "PlastIndia Foundation",
                        "Description": "Non-profit organization that promotes the development and growth of the plastics industry in India, including the recycling of various types of plastics, including LDPE.",
                        "Contact Number": "+91 22 26832911/14"
                    },
                    {
                        "Company": "Vimal International Private Limited",
                        "Description": "Renowned for Manufacturing, Exporting and Wholesaling Polythene sheets, Garbage Bag, Plastic Dana, Plastic Scrap, LDPE Plastic Roll, UV Transparent Sheet etc.",
                        "Email": "vimal.international@yahoo.in"
                    },
                    {
                        "Company": "Vandana Plastic Industries",
                        "Description": "Known to satisfactorily cater to the demands of its customer base in Magadi Main Road-Vijaynagar, Bangalore.",
                        "Contact Number": "094483 52799"
                    }
                ]
                st.title("LDPE Recycling Companies Information")
                st.write("Low-Density Polyethylene (LDPE) is a type of thermoplastic polymer that is widely used for its unique properties and versatility. LDPE is characterized by its low density and is made up of long chains of ethylene monomers, giving it a flexible and lightweight nature. It is commonly used for a variety of applications due to its excellent resistance to moisture, chemicals, and impact. LDPE is often used in the production of various plastic products, including plastic bags, plastic films, squeeze bottles, and containers. Another significant application of LDPE is in the construction industry, where it is used for cable insulation, geomembranes, and vapour barriers due to its water-resistant properties. Additionally, LDPE is utilized in the medical field for products like disposable gloves and medical packaging, as well as in the manufacturing of toys, tubing, and various consumer goods.")
                st.table(info_data)

        elif type == 'PS':
                    info_data = [
                    {
                        "Company": "NOVA Chemicals",
                        "Description": "Recycle PS for packaging materials such as foam trays, egg cartons, disposable cutlery, and protective packaging.",
                        "Contact Number": "403.750.3600"
                    },
                    {
                        "Company": "Pilot Corporation and Shachihata",
                        "Description": "Produce recycled PS-based writing instruments.",
                        "Email": "contactus@pilotcompany.com"
                    },
                    {
                        "Company": "Dart Container Corporation",
                        "Description": "Leading manufacturer of foam cups and containers with a recycling program for foam polystyrene products.",
                        "Contact Number": "(800) 248-5960"
                    },
                    {
                        "Company": "Agilyx Corporation",
                        "Description": "Focuses on advanced recycling technologies, converting difficult-to-recycle plastics like PS into valuable resources.",
                        "Contact Number": "503 217 3160"
                    },
                    {
                        "Company": "Styro-Genie",
                        "Description": "Specializes in processing foam polystyrene waste, reducing its volume and converting it into new products.",
                        "Contact Number": "295775166910"
                    }
                ]
                    st.title("Polystyrene (PS) Recycling Companies")
                    st.write("Polystyrene (PS) plastic is a versatile and widely used synthetic polymer known for its rigid and transparent properties. It comes in two main forms: general-purpose polystyrene (GPPS) and high-impact polystyrene (HIPS). GPPS is commonly used in packaging, disposable cutlery, and CD cases due to its clarity and ease of molding. HIPS, on the other hand, is blended with rubber to enhance its impact resistance, making it suitable for items like appliance housings and toys.")

                    st.table(info_data)
        elif type == 'PP':
            info_data = [
                    {
                        "Company": "Polywood and Green Tree Plastics",
                        "Description": "Focus on producing furniture made from recycled PP.",
                        "Email": "sales@greentreeplastics.com"
                    },
                    {
                        "Company": "NextLife and Unifi",
                        "Description": "Involved in PP recycling for textile applications.",
                        "Contact Number": "(800) 405-6308"
                    },
                    {
                        "Company": "KW Plastics and PureCycle Technologies",
                        "Description": "Specialize in recycling PP for packaging materials such as plastic containers, bottles, caps, and closures. No contact number and email ids available: Visit: https://www.kwplastics.com/contact-us/",
                        
                    },
                    {
                        "Company": "BASF India Limited",
                        "Description": "Subsidiary of BASF SE, involved in various sectors, including recycling PP plastic.",
                        "Email": "plasticizers.europe@basf.com"
                    },
                    {
                        "Company": "Biffa",
                        "Description": "UK-based waste management company that offers recycling services for PP plastic.",
                        "Contact Number": "0800 601 601"
                    }
                ]

                # Streamlit app
            st.title("PP Recycling Companies ")
            st.write("Polypropylene (PP) plastic is a versatile and widely used polymer known for its exceptional durability and heat resistance. It is derived from propylene monomers and is a part of the polyolefin family of plastics. PP is characterized by its high melting point, making it suitable for various applications where temperature resistance is crucial. It exhibits excellent chemical resistance, making it resistant to solvents and acids, and it has a relatively low density, which results in lightweight yet sturdy products. PP is commonly used in packaging, automotive parts, consumer goods, textiles, and medical devices due to its advantageous combination of properties. Its ability to be easily molded, fabricated, and recycled contributes to its popularity in both industrial and consumer sectors.")
            st.table(info_data)

        elif type == 'PVC':
            info_data = [
                    {
                        "Company": "Tarkett",
                        "Description": "Utilize recycled PVC in the production of vinyl flooring products such as tiles, sheets, and luxury vinyl planks.",
                        "Email": "saleshk@tarkett.com"
                    },
                    {
                        "Company": "Armstrong Flooring",
                        "Description": "Focus on utilizing recycled PVC in their flooring solutions.",
                        "Contact Number": "(098866 86665)"
                    },
                    {
                        "Company": "Deceuninck",
                        "Description": "Use recycled PVC in the manufacturing of new PVC window profiles.",
                        "Email": "info@deceuninck.in"
                    },
                    {
                        "Company": "Rehau",
                        "Description": "Emphasize the use of recycled PVC in their window systems.",
                        "Contact Number": "080 2222 0014"
                    },
                    {
                        "Company": "Recovinyl",
                        "Description": "An initiative in Europe to increase the collection and recycling of PVC materials.",
                        "Email": "info@recovinyl.com"
                    },
                    {
                        "Company": "Plastic Man",
                        "Description": "A plastic recycling company in India dealing with various types of plastic waste, including PVC.",
                        "Email": "plasticmanlv@gmail.com"
                    }
                ]

            st.title("PVC Recycling Companies")
            st.write("Polyvinyl chloride (PVC) is a versatile and widely used type of plastic polymer. It is known for its durability, versatility, and cost-effectiveness. PVC plastic can be found in a wide range of applications, including construction, electronics, automotive, healthcare, and more.")
            st.table(info_data)   
        elif type == 'PET':
                info_data = [
                    {
                        "Company": "Indian Oil Corporation (IOC)",
                        "Description": "IOC will recycle 100 million discarded mineral water, cold drink and PET bottles annually to make eco-friendly uniforms for staff that man its petrol pumps and LPG distributor agencies.",
                        "Contact Number": "011-71722285"
                    },
                    {
                        "Company": "Polycycle",
                        "Description": "Polycycle is a plastic recycling company transforming about 5.5 million PET bottles daily to make recycled polyester staple fibre.",
                        "Email": "info@polycycl.com"
                    },
                    {
                        "Company": "Visen Industries Limited",
                        "Description": "Visen Industries Limited produces PET resins and recycles PET plastics. They have a division called Visen Recycling that focuses on recycling PET and converting it into PET resins for various industrial applications.",
                        "Email": "accounts@visen.net"
                    },
                    {
                        "Company": "Reliance Industries Limited",
                        "Description": "Reliance Industries operates recycling facilities that process PET plastic bottles into recycled PET (rPET) resin, which can be used in various applications.",
                        "Contact Number": "+91 2222785000"
                    },
                    {
                        "Company": "Plastipak India",
                        "Description": "Plastipak is involved in PET recycling and uses collected PET bottles to produce rPET for packaging solutions.",
                        "Contact Number": "91-22-22840120"
                    },
                    {
                        "Company": "Agarwal Polyfill Pvt Ltd",
                        "Description": "Agarwal Polyfill Pvt Ltd is actively involved in the recycling industry, helping to address PET plastic pollution and promote responsible plastic waste management practices.",
                        "Email": "anup@rbagarwala.com"
                    }
                ]
                st.title("PET Companies Information")
                st.write("PET plastic, or Polyethylene Terephthalate, is a widely used thermoplastic polymer that is known for its clarity, strength, and versatility. It is commonly used in the manufacturing of various consumer goods, particularly beverage and food containers, such as water bottles, soda bottles, and food packaging. PET plastic is appreciated for its lightweight nature, making it convenient for single-use items and reducing transportation costs. Additionally, its high resistance to impact and moisture, along with its recyclability, contribute to its popularity.")
                st.table(info_data)
        elif type == 'OTHERS':
                    info_data = [
                        {
                            "Company": "Covestro",
                            "Description": "Recycle PC for automotive parts such as interior trims, dashboards, headlamp lenses, and exterior components.",
                            "Email": "puneet.kapur@covestro.com"
                        },
                        {
                            "Company": "Tuflite Polymers and Ajay Industrial Corporation",
                            "Description": "Offer PC-based construction materials like transparent roofing sheets, skylights, sound barriers, and safety glazing.",
                            "Email": "info@tuflite.com",
                            "Contact Number": "(91)-(120)-277 0679"
                        }
                    ]
                    st.title("OTHERS Recycling Companies ")
                    st.write("Plastics such as polycarbonate (PC) are versatile and durable thermoplastic polymers that find wide-ranging applications across various industries. Known for their exceptional impact resistance and optical clarity, PC plastics are commonly used in the production of items like eyewear lenses, safety goggles, medical devices, electronics, automotive components, and household appliances.")
                    st.table(info_data)
        st.button("Exit")
        if exit:
            st.session_state.page = "mainpage"
            #st.experimental_rerun()

def calculate_total_price(plastic_type, plastic_quantity):
    # Define prices for each plastic type (you can adjust these prices as needed)
    plastic_prices = {
        "HDPE": 90000,  # Price per ton for HDPE
        "LDPE": 80000,  # Price per ton for LDPE
        "OTHERS": 95000,  # Price per ton for OTHERS
        "PET": 75000,  # Price per ton for PET
        "PP": 85000,  # Price per ton for PP
        "PS": 82000,  # Price per ton for PS
        "PVC": 70000,  # Price per ton for PVC
    }

    # Calculate the total price based on the selected plastic type and quantity
    if plastic_type in plastic_prices:
        price_per_ton = plastic_prices[plastic_type]
        total_price = price_per_ton * plastic_quantity
        return total_price
    else:
        return None

def purchase():
    st.title("Plastic Order Form")
    with st.sidebar:
        st.title("Dashboard")
        if st.button("Prices"):
            st.session_state.page = "price"
            st.experimental_rerun()
        if st.button("Purchase"):
            st.session_state.page = "purchase"
            st.experimental_rerun()
    # Input fields
    plastic_type = st.selectbox("Select Plastic Type", ["HDPE", "LDPE", "OTHERS", "PET", "PP", "PS", "PVC"])
    plastic_quantity = st.number_input("Quantity of Plastic (in tons)", min_value=0)

    # Calculate total price when the user submits the form
    if st.button("Submit"):
        total_price = calculate_total_price(plastic_type, plastic_quantity)
        if total_price is not None:
            st.success(f"Total Price: Rs.{total_price:.2f}")

            # Add a button to redirect to the payment gateway
        st.button("Payment")
        if payment:
            st.session_state.page="payment"

def payment():

    st.title("Proceed to Pay")

    # Payment method selection
    payment_method = st.radio("Select Payment Method", ["Card Payment", "Cash on Delivery", "EMI", "UPI Payment"])

    # Display UI elements based on payment method selection
    if payment_method == "Card Payment":
        st.subheader("Card Payment")
        card_number = st.text_input("Card Number")
        expiration_date = st.text_input("Expiration Date (MM/YY)")
        cvv = st.text_input("CVV")
        
        # Proceed to Pay button for Card Payment
        if st.button("Proceed to Pay (Card Payment)"):
            st.success("Card Payment successful!")
            st.button("Exit")
            if exit:
                st.session_state.page="mainpage"
                #st.experimental_rerun()
    elif payment_method == "Cash on Delivery":
        st.subheader("Cash on Delivery")
        st.write("**Order Placed**")
        st.button("Exit")
        if exit:
            st.session_state.page="mainpage"
        
    elif payment_method == "EMI":
        st.subheader("EMI Payment")
        emi_options = st.selectbox("Select EMI Option", ["3 Months", "6 Months", "12 Months"])
        st.write(f"Selected EMI Option: {emi_options}")
        st.button("Exit")
        if exit:
            st.session_state.page="mainpage"

    # Conditional section for UPI Payment
    if payment_method == "UPI Payment":
        st.subheader("UPI Payment Options")
        
        # Display UPI payment app options
        selected_upi_app = st.selectbox("Select UPI Payment App", ["GPay", "PhonePe", "Paytm", "Other"])
        
        if st.button("Proceed to Pay (UPI Payment)"):
            if selected_upi_app == "GPay":
                # Redirect the user to GPay UPI payment page
                st.write("Redirecting to GPay UPI payment page...")
                # You would typically provide a UPI payment link or integrate with the GPay API for redirection.
                # Handle payment confirmation on your server after the payment is completed.
                st.success("UPI Payment successful!")
                st.button("Exit")
                if exit:
                    st.session_state.page="mainpage"

            # Add similar conditional sections for other UPI payment apps
            elif selected_upi_app == "PhonePe":
                # Redirect the user to PhonePe UPI payment page
                st.write("Redirecting to PhonePe UPI payment page...")
                # Handle payment confirmation on your server after the payment is completed.
                st.success("UPI Payment successful!")
                st.button("Exit")
                if exit:
                    st.session_state.page="mainpage"

            else:
                st.error("Please select a valid UPI payment app.")


  
def main():
    if not hasattr(st.session_state, "logged_in"):
        st.session_state.logged_in = False
    if "page" not in st.session_state:
        st.session_state.page = "mainpage"

    if st.session_state.page == "mainpage":
        main_page()
    elif st.session_state.page == "register":
        register()
    elif st.session_state.page == "login":
        login()
    elif st.session_state.page == "about":
        about()
    elif st.session_state.page == "contact":
        contact()
    elif st.session_state.page == "upload":
        upload()
    elif st.session_state.page == "details":
        details()
    elif st.session_state.page == "plastic":
        plastic()
    elif st.session_state.page == "price":
        price()
    elif st.session_state.page == "purchase":
        purchase()
    elif st.session_state.page == "payment":
        payment()
    elif st.session_state.page == "selling":
        selling()
if __name__ == "__main__":
    main()
