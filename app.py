import streamlit as st
import time
from PIL import Image as PILImage
from PIL import Image
import tensorflow as tf
import numpy as np

def about():
    with st.sidebar:
        st.title("Dashboard")
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
    st.write("Welcome to centralized repository for storing and organizing certificates accessed by both teachers and students. Here individual can enhance the efficiency, accuracy, and convenience of managing student certificates in educational institutions.Hence one can eliminate paper-based or scattered storage systems")
def contact():
    with st.sidebar:
        st.title("Dashboard")
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

    st.write("If you have any questions or need assistance, please feel free to contact our team:")

    profiles = [
        {
            "name": "XXX",
            "email": "xxx@gmail.com",
            "phone": "+1 (123) 456-7890",
            "image": "profile.webp",
        },
        {
            "name": "YYY",
            "email": "yyy@gmail.com",
            "phone": "+1 (987) 654-3210",
            "image": "profile.webp",
        },
        {
            "name": "ZZZ",
            "email": "zzz@gmail.com",
            "phone": "+1 (555) 123-4567",
            "image": "profile.webp",
        },
    ]
    cols = st.columns(len(profiles))
    for profile, col in zip(profiles,cols):
        st.subheader(profile["name"])
        image = PILImage.open(profile["image"])
        resized_image = st.image("profile.webp", width=150) 
        st.write("Email:", profile["email"])
        st.write("Phone:", profile["phone"])
        st.write("")

def main_page():
    st.title("Welcome to the PlasticCheckup")
    with st.sidebar:
        st.title("Dashboard")
        if st.button("Login", key="login_button"):
            st.session_state.page = "login"
            st.experimental_rerun()
        if st.button("About Us", key="about_button"):
            st.session_state.page = "about"
            st.experimental_rerun()
        if st.button("Contact Us", key="contact_button"):
            st.session_state.page = "contact"
            st.experimental_rerun()
    images = ['https://cdn3.mycity4kids.com/images/article-images/web/headersV2/img-20200711-5f09765eeeccb.jpg','https://newsmobile.in/wp-content/uploads/2017/04/20132F042F222F082Fearthdaynai.28961.jpg',
            'https://www.rts.com/wp-content/uploads/2020/10/shutterstock_1345281257_opt.jpg']
    image_placeholder = st.empty()
    while(True):
        for i in range(len(images)):
            image_placeholder.image(images[i], use_column_width=True, caption=f"Image {i+1}")
            time.sleep(3)

def login():
    with st.sidebar:
        st.title("Dashboard")
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
    email = st.text_input("Enter Email")
    ipass = st.text_input("Enter password", type="password")
    submit = st.button("Submit")

    if submit:
       st.session_state.page="upload"

# Load the trained model
model_path = "model.h5"
model = tf.keras.models.load_model(model_path)

# Preprocess the image for prediction
def preprocess_image(image):
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    return np.expand_dims(image_array, axis=0)

# Define the Streamlit app
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
        st.button("Next")
        if next:
            if type == 'HDPE':
                st.session_state.page="hdpe"
            elif type == 'LDPE':
                st.session_state.page="ldpe"
            elif type == 'PS':
                st.session_state.page="ps"
            elif type == 'PP':
                st.session_state.page="pp"
            elif type == 'PVC':
                st.session_state.page="pvc"
            elif type == 'PET':
                st.session_state.page="pet"
            elif type == 'OTHERS':
                st.session_state.page="others"



def hdpe():

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

    # Streamlit app
    st.title("HDPE Recycling Companies Information")
    st.write("High-Density Polyethylene (HDPE) is a versatile and widely used type of plastic known for its durability, strength, and resistance to various environmental factors. HDPE is a versatile plastic used in various applications, including packaging, pipes, toys, and household items. It has high strength and durability, making it suitable for products that require impact resistance, such as bottles for cleaning agents, milk jugs, and shampoo bottles. HDPE is more opaque than PET and is available in a variety of colours. It has excellent chemical resistance and is often used for storing chemicals, detergents, and other potentially reactive substances.")

    st.table(info_data)

def ldpe():
    # Information data
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

    # Streamlit app
    st.title("LDPE Recycling Companies Information")
    st.write("Low-Density Polyethylene (LDPE) is a type of thermoplastic polymer that is widely used for its unique properties and versatility. LDPE is characterized by its low density and is made up of long chains of ethylene monomers, giving it a flexible and lightweight nature. It is commonly used for a variety of applications due to its excellent resistance to moisture, chemicals, and impact. LDPE is often used in the production of various plastic products, including plastic bags, plastic films, squeeze bottles, and containers. Another significant application of LDPE is in the construction industry, where it is used for cable insulation, geomembranes, and vapour barriers due to its water-resistant properties. Additionally, LDPE is utilized in the medical field for products like disposable gloves and medical packaging, as well as in the manufacturing of toys, tubing, and various consumer goods.")

    st.table(info_data)

def pvc():
    # Information data
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

    # Streamlit app
    st.title("PVC Recycling Companies")
    st.write("Polyvinyl chloride (PVC) is a versatile and widely used type of plastic polymer. It is known for its durability, versatility, and cost-effectiveness. PVC plastic can be found in a wide range of applications, including construction, electronics, automotive, healthcare, and more.")

    st.table(info_data)

def pet():
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


    # Streamlit app
    st.title("PET Companies Information")
    st.write("PET plastic, or Polyethylene Terephthalate, is a widely used thermoplastic polymer that is known for its clarity, strength, and versatility. It is commonly used in the manufacturing of various consumer goods, particularly beverage and food containers, such as water bottles, soda bottles, and food packaging. PET plastic is appreciated for its lightweight nature, making it convenient for single-use items and reducing transportation costs. Additionally, its high resistance to impact and moisture, along with its recyclability, contribute to its popularity.")

    st.table(info_data)

def pp():
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

def ps():
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

    # Streamlit app
    st.title("Polystyrene (PS) Recycling Companies")
    st.write("Polystyrene (PS) plastic is a versatile and widely used synthetic polymer known for its rigid and transparent properties. It comes in two main forms: general-purpose polystyrene (GPPS) and high-impact polystyrene (HIPS). GPPS is commonly used in packaging, disposable cutlery, and CD cases due to its clarity and ease of molding. HIPS, on the other hand, is blended with rubber to enhance its impact resistance, making it suitable for items like appliance housings and toys.")

    st.table(info_data)

def others():
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

    # Streamlit app
    st.title("OTHERS Recycling Companies ")
    st.write("Plastics such as polycarbonate (PC) are versatile and durable thermoplastic polymers that find wide-ranging applications across various industries. Known for their exceptional impact resistance and optical clarity, PC plastics are commonly used in the production of items like eyewear lenses, safety goggles, medical devices, electronics, automotive components, and household appliances.")


    # Display the DataFrame without index column
    st.table(info_data)
def main():
    if not hasattr(st.session_state, "logged_in"):
        st.session_state.logged_in = False
    if "page" not in st.session_state:
        st.session_state.page = "main"

    if st.session_state.page == "main":
        main_page()
    elif st.session_state.page == "login":
        login()
    elif st.session_state.page == "about":
        about()
    elif st.session_state.page == "contact":
        contact()
    elif st.session_state.page == "upload":
        upload()
    elif st.session_state.page == "hdpe":
        hdpe()
    elif st.session_state.page == "ldpe":
        ldpe()
    elif st.session_state.page == "ps":
        ps()
    elif st.session_state.page == "pp":
        pp()
    elif st.session_state.page == "pet":
        pet()
    elif st.session_state.page == "pvc":
        pvc()
    elif st.session_state.page == "others":
        others()

if __name__ == "__main__":
    main()