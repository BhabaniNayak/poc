
prompt_id = """
    Generate a personalized email campaign message using the following inputs:

    - User ID: [User ID]
    - Funnel Stage: [Funnel Stage]
    - UTM Source: [UTM Source]
    - Product: [Product]
    - User Persona: [User Persona]
    - Interest: [Interest]

    
    Intent: Persuade, be creative, and use compelling language to convince the user to purchase the product.

    Example input 1:
        Generate a personalized email campaign message using the following inputs:

        - User ID: 123456789
        - Funnel Stage: Consideration
        - UTM Source: Display Ad from Google
        - Product: Google Pixel 4
        - User Persona: Tech Savvy
        - Interest: Gadgets
        - Intent: Persuade, be creative, and use compelling language to convince the user to purchase the product or service.
    
    Example output 1:
        Subject: Your Ultimate Tech Companion is Here! Exclusive Offer Inside.

        Dear [User ID],

        We're excited to present you with an exclusive opportunity to own the latest and greatest gadget in the tech world: the all-new Google Pixel 4! As a tech-savvy individual with a passion for gadgets, this device is tailored to elevate your digital experience to new heights.

        At this consideration stage, we understand that you're actively exploring your options. That's why we wanted to reach out to you after seeing your interest in gadgets through our Google Display Ad. We believe the Google Pixel 4 is the perfect companion for someone like you who values innovation, performance, and cutting-edge technology.

        With its advanced features, stunning camera capabilities, and seamless integration with your digital lifestyle, the Google Pixel 4 is designed to exceed your expectations. Capture breathtaking photos, enjoy a smooth and intuitive user experience, and stay ahead of the curve with its powerful performance.

        As a valued tech enthusiast, we're offering you an exclusive discount on the Google Pixel 4 when you purchase through our website. This limited-time offer is our way of showing appreciation for your passion for technology. Don't miss out on this opportunity to be one of the first to experience the future of smartphones.

        Visit our website using the link below to unlock this exclusive offer and discover why the Google Pixel 4 is the ultimate choice for tech-savvy individuals like yourself:

        [Insert Website Link]

        We're confident that the Google Pixel 4 will exceed your expectations and become your trusted companion in the digital world. Don't just follow the latest trends, embrace them with this cutting-edge device that combines style, functionality, and innovation.

        If you have any questions or need further assistance, our dedicated support team is here to help. Feel free to reach out to us at [Contact Email or Phone Number].

        Thank you for considering the Google Pixel 4 as your next gadget. Act fast and take advantage of this exclusive offer before it's too late!

        Best regards,

        [Your Company Name]


    Example input 2:

        Generate a personalized email campaign message using the following inputs:

        - User ID: 987654321
        - Funnel Stage: Awareness
        - UTM Source: Email
        - Product: L'Oreal Paris Mascara
        - User Persona: Budget Conscious
        - Interest: cosmetics
        - Intent: Persuade, be creative, and use compelling language to convince the user to purchase the product or service.
    
    Example output 2:
        Subject: Discover Your Perfect Lashes with L'Oreal Paris Mascara - Exclusive Offer Inside!

        Dear [User ID],

        We hope this email finds you well and ready to elevate your beauty game to new heights. As a valued customer, we know that cosmetics play a significant role in expressing your unique style and enhancing your natural beauty. That's why we're excited to introduce you to our best-selling L'Oreal Paris Mascara.

        Imagine having long, voluminous lashes that make your eyes pop and leave a lasting impression. Our mascara is designed to give you that coveted, dramatic look without breaking the bank. With its innovative formula and precision brush, it effortlessly coats each lash, delivering intense length and incredible volume.

        We understand that being budget-conscious is important to you, which is why we're delighted to offer you an exclusive discount on our L'Oreal Paris Mascara. Don't miss out on this opportunity to achieve stunning lashes while saving on your beauty essentials.

        Upgrade your makeup routine and embrace the confidence that comes with perfectly defined lashes. Click the link below to explore our range of L'Oreal Paris Mascaras and claim your special discount:

        [Insert Call-to-Action Button: Shop Now]

        We're confident that our L'Oreal Paris Mascara will exceed your expectations and become your go-to beauty staple. Join countless satisfied customers who have already experienced the transformative power of our mascara.

        Indulge in the world of exquisite lashes and embrace the beauty that lies within you. We can't wait to see you radiate with confidence and style!

        Best regards,

        [Your Name]
        [Your Title]
        [Company Name]
"""

sample_prompt = """        

    Generate a personalized email campaign message using the following inputs:

        - User ID: 123456789
        - Funnel Stage: Consideration
        - UTM Source: Display Ad from Google
        - Product: Google Pixel 4
        - User Persona: Tech Savvy
        - Interest: Gadgets
        - Intent: Persuade, be creative, and use compelling language to convince the user to purchase the product or service.
"""