def email_subject_template(name, website, has_website):
    if has_website:
        return f"""Have been looking at {name}'s website.."""
    else:
        return f"""Interested in a website or mobile app to feature your business?"""


def create_email_template(to_management, my_name, colleagues, i_love, the_first, first_impressions, i_am_confident,
                          closing):
    return (f"""
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
	<head>
	<link href="https://fonts.googleapis.com/css?family=Helvetica:400,400i,700,700i&amp;subset=latin-ext" rel="stylesheet">
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
		<title>Matthew Muscat | Website Development & Mobile Apps</title>

	<style type="text/css">

			/* ----- Text Styles ----- */
			table{{
				font-family: 'Helvetica';
				-webkit-font-smoothing: antialiased;
				-moz-font-smoothing: antialiased;
				font-smoothing: antialiased;
				text-decoration:none
			}}

			@media only screen and (max-width: 700px){{
				/* ----- Base styles ----- */
				.full-width-container{{
					padding: 0 !important;
				}}

				.container{{
					width: 100% !important;
				}}

				/* ----- Header ----- */
				.header td{{
					padding: 30px 30px 30px 15px !important;
				}}

				/* ----- Projects list ----- */
				.projects-list{{
					display: block !important;
				}}

				.projects-list tr{{
					display: block !important;
				}}

				.projects-list td{{
					display: block !important;
				}}

				.projects-list tbody{{
					display: block !important;
				}}

				.projects-list img{{
					margin: 0 auto 25px auto;
				}}

				/* ----- Half block ----- */
				.half-block{{
					display: block !important;
				}}

				.half-block tr{{
					display: block !important;
				}}

				.half-block td{{
					display: block !important;
				}}

				.half-block__image{{
					width: 100% !important;
					background-size: cover;
				}}

				.half-block__content{{
					width: 100% !important;
					box-sizing: border-box;
					padding: 25px 15px 25px 15px !important;
				}}

				/* ----- Hero subheader ----- */
				.hero-subheader__title{{
					padding: 35px 15px 15px 15px !important;
					font-size: 25px !important;
				}}

				.hero-subheader__content{{
					padding: 0 15px 30px 15px !important;
				}}

				/* ----- Title block ----- */
				.title-block{{
					padding: 0 15px 0 15px;
				}}

				/* ----- Paragraph block ----- */
				.paragraph-block__content{{
					padding: 25px 15px 18px 15px !important;
				}}

				/* ----- Info bullets ----- */
				.info-bullets{{
					display: block !important;
				}}

				.info-bullets tr{{
					display: block !important;
				}}

				.info-bullets td{{
					display: block !important;
				}}

				.info-bullets tbody{{
					display: block;
				}}

				.info-bullets__icon{{
					text-align: center;
					padding: 0 0 15px 0 !important;
				}}

				.info-bullets__content{{
					text-align: center;
				}}

				.info-bullets__block{{
					padding: 25px !important;
				}}

				/* ----- CTA block ----- */
				.cta-block__title{{
					padding: 35px 15px 0 15px !important;
				}}

				.cta-block__content{{
					padding: 20px 15px 27px 15px !important;
				}}

				.cta-block__button{{
					padding: 0 15px 0 15px !important;
				}}
			}}
		</style>
	</head>

	<body style="padding: 0; margin: 0;" bgcolor="#eeeeee">
		<span style="color:transparent !important; overflow:hidden !important; display:none !important; line-height:0px !important; height:0 !important; opacity:0 !important; visibility:hidden !important; width:0 !important; mso-hide:all;">Matthew</span>

		<!-- / Full width container -->
		<table class="full-width-container" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" bgcolor="#eeeeee" style="width: 100%; height: 100%; padding: 30px 0 30px 0; font-family: 'Helvetica';
				-webkit-font-smoothing: antialiased;
				-moz-font-smoothing: antialiased;
				font-smoothing: antialiased;">
			<tr>
				<td align="center" valign="top">
					<!-- / 700px container -->
					<table class="container" border="0" cellpadding="0" cellspacing="0" width="700" bgcolor="#ffffff" style="width: 1000px; font-family: 'Helvetica';
				-webkit-font-smoothing: antialiased;
				-moz-font-smoothing: antialiased;
				font-smoothing: antialiased;">
						<tr>
							<td align="center" valign="top">
								<!-- / Header -->
								<table class="container header" border="0" cellpadding="0" cellspacing="0" width="620" style="width: 920px; font-family: 'Helvetica';
				-webkit-font-smoothing: antialiased;
				-moz-font-smoothing: antialiased;
				font-smoothing: antialiased;">
									<tr>
										<td style="padding: 50px 0 30px 0px; border-bottom: solid 1px #eeeeee;" align="left">
											<img src="https://www.matthewmuscat.com.au/images/matthewmuscat.com.au.png">
										</td>
									</tr>
								</table>
								<!-- /// Header -->

								<!-- / Hero subheader -->
								<table class="container hero-subheader" border="0" cellpadding="0" cellspacing="0" width="620" style="width: 920px; font-family: 'Helvetica';
				-webkit-font-smoothing: antialiased;
				-moz-font-smoothing: antialiased;
				font-smoothing: antialiased;">
									<tr>
										<td class="hero-subheader__title" style="font-size: 20px; font-weight: bold; padding: 30px 0 15px 0;" align="left">{to_management}</td>
									</tr>

									<tr>
										<td class="hero-subheader__content" style="font-size: 16px; line-height: 27px; color: #707070; padding: 0 60px 5px 0;" align="left">

									{my_name}
									{colleagues}
									{i_love}
									{the_first}
									{first_impressions}
									{i_am_confident}
									{closing}

									</td>
									</tr>
								</table>
								<!-- /// Hero subheader -->


								<!-- / Divider -->
								<table class="container" border="0" cellpadding="0" cellspacing="0" width="100%" style="padding-top: 25px; font-family: 'Helvetica';
				-webkit-font-smoothing: antialiased;
				-moz-font-smoothing: antialiased;
				font-smoothing: antialiased;" align="center">
									<tr>
										<td align="center">
											<table class="container" border="0" cellpadding="0" cellspacing="0" width="620" align="center" style="border-bottom: solid 1px #eeeeee; width: 920px;">
												<tr>
													<td align="center">&nbsp;</td>
												</tr>
											</table>
										</td>
									</tr>
								</table>


								<table class="container hero-subheader" border="0" cellpadding="0" cellspacing="0" width="620" style="width: 920px; font-family: 'Helvetica';
				-webkit-font-smoothing: antialiased;
				-moz-font-smoothing: antialiased;
				font-smoothing: antialiased;">


									<tr>
										<td class="hero-subheader__content" style="font-size: 16px; line-height: 27px; color: #707070; padding: 0 60px 5px 0;" align="center">

										<br>Mobile Number: 0439 386 998<br>
										Email: mail@matthewmuscat.com.au<br>
										Website: www.matthewmuscat.com.au<br><br>

									</td>
									</tr>
								</table>

								<!-- /// Footer -->

				</td>
			</tr>
		</table>
	</body>
</html>""")




def email_subject_if_sent():
	return f"""Apologies, email provider has had some issues."""


def email_msg_if_sent(name):
	return f"""To management of {name},<br><br>
We have been experiencing some issues with our email provider that has caused problems with receiving replies.
If you have tried to get in contact through email, it would not have came through on our end. This has now been fixed, so feel free to reply directly to this email and we can continue business. 
Sorry for the inconvenience.<br><br>
Kind Regards,<br>

Matthew Muscat<br><br>

Mobile Number: 0439 386 998<br>
Email: mail@matthewmuscat.com.au<br>
Website: www.matthewmuscat.com.au"""


def email_message_template(name, website, has_website, location, business_type, demo):
    to_management = f'To management of {name},<br>'
    rest_mackay_website = [
        f'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for <a href="http://www.roshni.com.au/">Roshni Indian Restaurant</a> in Mackay and wanted to reach out to similar companies.'
        ,
        'You can also find my past work at my website <a href="https://www.matthewmuscat.com.au/">here</a>.<br><br>I love the atmosphere provided by your current online platforms and your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. However, I think your website has room for improvement. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.<br><br>'
        ,
        'The first action a potential customer undertakes when looking for somewhere to eat out, is browse a popular platform such as Trip Advisor or Google Maps where they will be directed to the restaurants website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        'I am confident that if we work together, I could help to improve your platform, in terms of functionality and aesthetics, so that we can maximise your restaurants visibility online.<br><br>']

    rest_mackay = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for <a href="http://www.roshni.com.au/">Roshni Indian Restaurant</a> in Mackay and wanted to reach out to similar companies.'
        ,
        'You can also find my past work at my website <a href="https://www.matthewmuscat.com.au/">here</a>.<br><br>I love the atmosphere provided by your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. I notice that your business does not have a website, or much of a digital environment at all. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.<br><br>'
        ,
        'The first action a potential customer undertakes when looking for somewhere to eat out, is browse a popular platform such as Trip Advisor or Google Maps where they will be directed to the restaurants website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        'I am confident that if we work together, I could help to create your platform consisting of a modern appeal that will stand out against your competitors, so that we can maximise your restaurants visibility online.<br><br>']

    rest_anywhere_website = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for <a href="http://www.roshni.com.au/">Roshni Indian Restaurant</a> and wanted to reach out to similar companies.'
        ,
        'You can also find my past work at my website <a href="https://www.matthewmuscat.com.au/">here</a>.<br><br>I love the atmosphere provided by your current online platforms and your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. However, I think your website has room for improvement. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.<br><br>'
        ,
        'The first action a potential customer undertakes when looking for somewhere to eat out, is browse a popular platform such as Trip Advisor or Google Maps where they will be directed to the restaurants website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        'I am confident that if we work together, I could help to improve your platform, in terms of functionality and aesthetics, so that we can maximise your restaurants visibility online.<br><br>']

    rest_anywhere = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for <a href="http://www.roshni.com.au/">Roshni Indian Restaurant</a> and wanted to reach out to similar companies.'
        ,
        'You can also find my past work at my website <a href="https://www.matthewmuscat.com.au/">here</a>.<br><br>I love the atmosphere provided by your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. I notice that your business does not have a website, or much of a digital environment at all. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.<br><br>'
        ,
        'The first action a potential customer undertakes when looking for somewhere to eat out, is browse a popular platform such as Trip Advisor or Google Maps where they will be directed to the restaurants website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        'I am confident that if we work together, I could help to create your platform consisting of a modern appeal that will stand out against your competitors, so that we can maximise your restaurants visibility online.<br><br>']

    anything_mackay_website = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for <a href="http://www.roshni.com.au/">Roshni Indian Restaurant</a> in Mackay and wanted to reach out to similarly located companies. '
        ,
        'You can also find my past work at my website <a href="https://www.matthewmuscat.com.au/">here</a>.<br><br>I love the atmosphere provided by your current online platforms and your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. However, I think your website has room for improvement. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.<br><br>'
        ,
        'The first action a potential customer undertakes when looking for a business to service their needs, is browse a popular platform such as Google Maps where they will be directed to the company’s website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        "I am confident that if we work together, I could help to improve your platform, in terms of functionality and aesthetics, so that we can maximise your business' visibility online.<br><br>"]

    anything_mackay = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for <a href="http://www.roshni.com.au/">Roshni Indian Restaurant</a> in Mackay and wanted to reach out to similarly located companies.'
        ,
        'You can also find my past work at my website <a href="https://www.matthewmuscat.com.au/">here</a>.<br><br>I love the atmosphere provided by your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. I notice that your business does not have a website, or much of a digital environment at all. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.<br><br>'
        ,
        'The first action a potential customer undertakes when looking for a business to service their needs, is browse a popular platform such as Google Maps where they will be directed to the company’s website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        "I am confident that if we work together, I could help to create your platform consisting of a modern appeal that will stand out against your competitors, so that we can maximise your business' visibility online.<br><br>"]

    anything_anywhere_website = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for <a href="http://www.roshni.com.au/">Roshni Indian Restaurant</a> and wanted to reach out to similar companies.'
        ,
        'You can also find my past work at my website <a href="https://www.matthewmuscat.com.au/">here</a>.<br><br>I love the atmosphere provided by your current online platforms and your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. However, I think your website has room for improvement. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.<br><br>'
        ,
        'The first action a potential customer undertakes when looking for a business to service their needs, is browse a popular platform such as Google Maps where they will be directed to the company’s website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        "I am confident that if we work together, I could help to improve your platform, in terms of functionality and aesthetics, so that we can maximise your business' visibility online.<br><br>"]

    anything_anywhere = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for <a href="http://www.roshni.com.au/">Roshni Indian Restaurant</a> and wanted to reach out to similarly located companies.'
        ,
        'You can also find my past work at my website <a href="https://www.matthewmuscat.com.au/">here</a>.<br><br>I love the atmosphere provided by your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. I notice that your business does not have a website, or much of a digital environment at all. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.<br><br>'
        ,
        'The first action a potential customer undertakes when looking for a business to service their needs, is browse a popular platform such as Google Maps where they will be directed to the company’s website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        "I am confident that if we work together, I could help to create your platform consisting of a modern appeal that will stand out against your competitors, so that we can maximise your business' visibility online.<br><br>"]

    colleagues = f"One of my colleagues is a loyal customer to your business, and she recommended that I reach out to see if you might be interested in a similar product. I have gone ahead and used one of my existing designs to create a mockup website for your business. Please note that the purpose of this demo is to demonstrate an example of what I can do for you if we work together. Recognise that it is design focused and irrespective of personalised content.<br><br><a href='{demo}'>Please see {name}'s demo page here.</a><br>"
    closing = f"""I've spent the past years helping various companies in {location} create products which have shown sales growth and have improved the overall interaction they have with the community. I'm a one-man venture, and I only take on one job at a time. This ensures that you will have my undivided attention while I work on your project, and also allows me to offer the service at a greatly reduced price.<br><br>
    If you wish to see some of my past work, please visit my website found below.<br>
    Let me know if you find this interesting, and I would be happy to contact you so we can have a chat over the phone.<br><br>
    Kind Regards,<br>
    Matthew Muscat"""

    if location == "Mackay QLD" and business_type == "restaurants" and has_website:
        return create_email_template(to_management, rest_mackay_website[0], colleagues, rest_mackay_website[1],
                                     rest_mackay_website[2], rest_mackay_website[3], rest_mackay_website[4], closing)

    elif location == "Mackay QLD" and business_type == "restaurants" and not has_website:
        return create_email_template(to_management, rest_mackay[0], colleagues, rest_mackay[1], rest_mackay[2],
                                     rest_mackay[3], rest_mackay[4], closing)

    elif location != "Mackay QLD" and business_type == "restaurants" and has_website:
        return create_email_template(to_management, rest_anywhere_website[0], colleagues, rest_anywhere_website[1],
                                     rest_anywhere_website[2], rest_anywhere_website[3], rest_anywhere_website[4],
                                     closing)

    elif location != "Mackay QLD" and business_type == "restaurants" and not has_website:
        return create_email_template(to_management, rest_anywhere[0], colleagues, rest_anywhere[1], rest_anywhere[2],
                                     rest_anywhere[3], rest_anywhere[4], closing)

    elif location == "Mackay QLD" and business_type != "restaurants" and has_website:
        return create_email_template(to_management, anything_mackay_website[0], colleagues, anything_mackay_website[1],
                                     anything_mackay_website[2], anything_mackay_website[3], anything_mackay_website[4],
                                     closing)

    elif location == "Mackay QLD" and business_type != "restaurants" and not has_website:
        return create_email_template(to_management, anything_mackay[0], colleagues, anything_mackay[1],
                                     anything_mackay[2], anything_mackay[3], anything_mackay[4], closing)

    elif location != "Mackay QLD" and business_type != "restaurants" and has_website:
        return create_email_template(to_management, anything_anywhere_website[0], colleagues,
                                     anything_anywhere_website[1], anything_anywhere_website[2],
                                     anything_anywhere_website[3], anything_anywhere_website[4], closing)

    elif location != "Mackay QLD" and business_type != "restaurants" and not has_website:
        return create_email_template(to_management, anything_anywhere[0], colleagues, anything_anywhere[1],
                                     anything_anywhere[2], anything_anywhere[3], anything_anywhere[4], closing)


def email_message_template_text(name, website, has_website, location, business_type, demo):
    to_management = f'To management of {name},\n'
    rest_mackay_website = [
        f'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for Roshni Indian Restaurant (www.roshni.com.au) in Mackay and wanted to reach out to similar companies.'
        ,
        f'You can also find my past work at my website (https://www.matthewmuscat.com.au/).\n\nI love the atmosphere provided by your current online platforms and your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. However, I think your website has room for improvement. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.\n'
        ,
        'The first action a potential customer undertakes when looking for somewhere to eat out, is browse a popular platform such as Trip Advisor or Google Maps where they will be directed to the restaurants website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        'I am confident that if we work together, I could help to improve your platform, in terms of functionality and aesthetics, so that we can maximise your restaurants visibility online.']

    rest_mackay = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for Roshni Indian Restaurant (www.roshni.com.au) in Mackay and wanted to reach out to similar companies.'
        ,
        f'You can also find my past work at my website (https://www.matthewmuscat.com.au/).\n\nI love the atmosphere provided by your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. I notice that your business does not have a website, or much of a digital environment at all. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.\n'
        ,
        'The first action a potential customer undertakes when looking for somewhere to eat out, is browse a popular platform such as Trip Advisor or Google Maps where they will be directed to the restaurants website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        'I am confident that if we work together, I could help to create your platform consisting of a modern appeal that will stand out against your competitors, so that we can maximise your restaurants visibility online.']

    rest_anywhere_website = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for Roshni Indian Restaurant (www.roshni.com.au) and wanted to reach out to similar companies.'
        ,
        f'You can also find my past work at my website (https://www.matthewmuscat.com.au/).\n\nI love the atmosphere provided by your current online platforms and your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. However, I think your website has room for improvement. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.\n'
        ,
        'The first action a potential customer undertakes when looking for somewhere to eat out, is browse a popular platform such as Trip Advisor or Google Maps where they will be directed to the restaurants website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        'I am confident that if we work together, I could help to improve your platform, in terms of functionality and aesthetics, so that we can maximise your restaurants visibility online.']

    rest_anywhere = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for Roshni Indian Restaurant (www.roshni.com.au) and wanted to reach out to similar companies.'
        ,
        f'You can also find my past work at my website (https://www.matthewmuscat.com.au/).\n\nI love the atmosphere provided by your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. I notice that your business does not have a website, or much of a digital environment at all. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.\n'
        ,
        'The first action a potential customer undertakes when looking for somewhere to eat out, is browse a popular platform such as Trip Advisor or Google Maps where they will be directed to the restaurants website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        'I am confident that if we work together, I could help to create your platform consisting of a modern appeal that will stand out against your competitors, so that we can maximise your restaurants visibility online.']

    anything_mackay_website = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for Roshni Indian Restaurant (www.roshni.com.au) in Mackay and wanted to reach out to similarly located companies.'
        ,
        f'You can also find my past work at my website (https://www.matthewmuscat.com.au/).\n\nI love the atmosphere provided by your current online platforms and your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. However, I think your website has room for improvement. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.\n'
        ,
        'The first action a potential customer undertakes when looking for a business to service their needs, is browse a popular platform such as Google Maps where they will be directed to the company’s website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        "I am confident that if we work together, I could help to improve your platform, in terms of functionality and aesthetics, so that we can maximise your business' visibility online."]

    anything_mackay = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for Roshni Indian Restaurant (www.roshni.com.au) in Mackay and wanted to reach out to similarly located companies.'
        ,
        f'You can also find my past work at my website (https://www.matthewmuscat.com.au/).\n\nI love the atmosphere provided by your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. I notice that your business does not have a website, or much of a digital environment at all. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.\n'
        ,
        'The first action a potential customer undertakes when looking for a business to service their needs, is browse a popular platform such as Google Maps where they will be directed to the company’s website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        "I am confident that if we work together, I could help to create your platform consisting of a modern appeal that will stand out against your competitors, so that we can maximise your business' visibility online."]

    anything_anywhere_website = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for Roshni Indian Restaurant (www.roshni.com.au) and wanted to reach out to similar companies.'
        ,
        f'You can also find my past work at my website (https://www.matthewmuscat.com.au/).\n\nI love the atmosphere provided by your current online platforms and your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. However, I think your website has room for improvement. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.\n'
        ,
        'The first action a potential customer undertakes when looking for a business to service their needs, is browse a popular platform such as Google Maps where they will be directed to the company’s website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        "I am confident that if we work together, I could help to improve your platform, in terms of functionality and aesthetics, so that we can maximise your business' visibility online."]

    anything_anywhere = [
        'My name is Matthew Muscat. I’m a website and mobile app developer, and recently I finished up a website design project for Roshni Indian Restaurant (www.roshni.com.au) and wanted to reach out to similarly located companies.'
        ,
        f'You can also find my past work at my website (https://www.matthewmuscat.com.au/).\nI love the atmosphere provided by your commitment to an active social engagement, especially through social media where I see you have gotten many positive reviews. I notice that your business does not have a website, or much of a digital environment at all. Customers today expect a modern standard using the latest technologies, and it has been documented that the smallest user experience improvements can lead to significant increases in engagement and sales.\n'
        ,
        'The first action a potential customer undertakes when looking for a business to service their needs, is browse a popular platform such as Google Maps where they will be directed to the company’s website.'
        ,
        f'First impressions are everything - and with a little research it can be found that the majority of websites in the {business_type} category within {location} have very outdated and poorly made websites, making it very easy to stand out.'
        ,
        "I am confident that if we work together, I could help to create your platform consisting of a modern appeal that will stand out against your competitors, so that we can maximise your business' visibility online."]

    colleagues = f'One of my colleagues is a loyal customer to your business, and she recommended that I reach out to see if you might be interested in a similar product. I have gone ahead and used one of my existing designs to create a mockup website for your business. Please note that the purpose of this demo is to demonstrate an example of what I can do for you if we work together. Recognise that it is design focused and irrespective of personalised content.\n\n{demo}.\n'
    closing = f"""\nI've spent the past years helping various companies in {location} create products which have shown sales growth and have improved the overall interaction they have with the community. I'm a one-man venture, and I only take on one job at a time. This ensures that you will have my undivided attention while I work on your project, and also allows me to offer the service at a greatly reduced price.\n
If you wish to see some of my past work, please visit my website at www.matthewmuscat.com.au.
Let me know if you find this interesting, and I would be happy to contact you so we can have a chat over the phone.\n
Kind Regards,
Matthew Muscat

Mobile Number: Mobile
Email: email
Website: www.matthewmuscat.com.au\n\n"""

    if location == "Mackay QLD" and business_type == "restaurants" and has_website:
        return f"""{to_management}
{rest_mackay_website[0]} {colleagues}
{rest_mackay_website[1]}
{rest_mackay_website[2]}{rest_mackay_website[3]}{rest_mackay_website[4]}
{closing}"""

    elif location == "Mackay QLD" and business_type == "restaurants" and not has_website:
        return f"""{to_management }
{rest_mackay[0]} {colleagues}
{rest_mackay[1]} 
{rest_mackay[2]}{rest_mackay[3]}{rest_mackay[4]} 
{closing}"""

    elif location != "Mackay QLD" and business_type == "restaurants" and has_website:
        return f"""{to_management }
{rest_anywhere_website[0]} {colleagues}
{rest_anywhere_website[1]} 
{rest_anywhere_website[2]}{rest_anywhere_website[3]}{rest_anywhere_website[4]} 
{closing}"""

    elif location != "Mackay QLD" and business_type == "restaurants" and not has_website:
        return f"""{to_management}
{rest_anywhere[0]} {colleagues}
{rest_anywhere[1]} 
{rest_anywhere[2]}{rest_anywhere[3]}{rest_anywhere[4]} 
{closing}"""

    elif location == "Mackay QLD" and business_type != "restaurants" and has_website:
        return f"""{to_management}
{anything_mackay_website[0]} {colleagues}
{anything_mackay_website[1]} 
{anything_mackay_website[2]}{anything_mackay_website[3]}{anything_mackay_website[4]} 
{closing}"""

    elif location == "Mackay QLD" and business_type != "restaurants" and not has_website:
        return f"""{to_management}
{anything_mackay[0]} {colleagues}
{anything_mackay[1]} 
{anything_mackay[2]}{anything_mackay[3]}{anything_mackay[4]} 
{closing}"""

    elif location != "Mackay QLD" and business_type != "restaurants" and has_website:
        return f"""{to_management}
{anything_anywhere_website[0]} {colleagues}
{anything_anywhere_website[1]} 
{anything_anywhere_website[2]}{anything_anywhere_website[3]}{anything_anywhere_website[4]} 
{closing}"""

    elif location != "Mackay QLD" and business_type != "restaurants" and not has_website:
        return f"""{to_management}
{anything_anywhere[0]} {colleagues}
{anything_anywhere[1]} 
{anything_anywhere[2]}{anything_anywhere[3]}{anything_anywhere[4]} 
{closing}"""
