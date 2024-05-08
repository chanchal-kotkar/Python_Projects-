from flask import Flask, redirect, request
import stripe

app = Flask(__name__,static_url_path="",static_folder="public")


stripe.api_key = "sk_test_51PBVpMSC8MCqitwLyabILOIJuO3ObEkQnIMuLvrWhvNajv6aw3Qj1RkaD4cj298V9lpcdd8A4sgjqn8AbvjqMgut00M7d4SzXb"
YOUR_DOMAIN ="http://localhost:5000"


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:

        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    "price":'price_1PBx2ZSC8MCqitwLsBk8me17',
                    "quantity" : 1
                }
            ],
            mode="subscription",
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + "/cancel.html"
        )

    except Exception as e:
        return str(e)    


    return redirect(checkout_session.url,code=303)



if __name__=="__main__":
    app.run(port=5000,debug=True)