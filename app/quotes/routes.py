from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify
from flask_login import current_user, login_required
from app import db
from app.models import Quote, UserProfile
from app.quotes.forms import QuoteForm

quotes = Blueprint('quotes', __name__)


@quotes.route("/quote/new", methods=['GET', 'POST'])
@login_required
def new_quote():
    if not current_user.user_profile:
        return redirect(url_for('users.account'))

    else:
        form = QuoteForm()
        if form.validate_on_submit():
            quote = Quote(
                author=current_user,
                gallons_requested=form.gallons_requested.data,
                date_requested=form.date_requested.data,
                delivery_address=form.delivery_address.data,
                suggested_price=form.suggested_price.data,
                total_amount_due=form.total_amount_due.data,
            )
            if form.get_quote.data:
                # quote = Quote(
                #     author=current_user,
                #     gallons_requested=form.gallons_requested.data,
                #     date_requested=form.date_requested.data,
                #     delivery_address=form.delivery_address.data,
                #     suggested_price=form.suggested_price.data,
                #     total_amount_due=form.total_amount_due.data,
                # )
                db.session.add(quote)
                db.session.commit()
                flash('Your quote has been saved', 'success')
                return redirect(url_for('main.home'))
            elif form.get_price.data:
                if current_user.user_profile.state == 'TX':
                    location_factor = 0.02
                else:
                    location_factor = 0.04

                # exists = db.session.query(db.exists().where(current_user.id == current_user.quotes.user_id)).scalar()
                #
                # if exists:
                #     rate_factor = 0.01
                # elif not exists:
                #     rate_factor = 0
                rate_factor = 0

                if form.gallons_requested.data > 1000:
                    gallons_requested_factor = 0.02
                else:
                    gallons_requested_factor = 0.03

                date = str(request.form['date_requested'])

                year, month, datee = date.split("-")
                month = int(month)

                if month in range(3, 9):
                    rate_fluctuation = 0.04
                else:
                    rate_fluctuation = 0.03

                currentprice = 1.50
                company_profit_factor = 0.1

                margin = currentprice * (
                        location_factor - rate_factor + gallons_requested_factor + company_profit_factor +
                        rate_fluctuation)

                gallons = request.form['gallons_requested']
                suggestedprice = float(currentprice) + margin
                totalamt = float(gallons) * suggestedprice
                # return jsonify({'suggested_price': suggestedprice}, {'total_amount_due': totalamt})
                return jsonify({'suggested_price': suggestedprice}, {'total_amount_due': totalamt})
            return jsonify(data=form.errors)

            # flash('Price', 'success')
            # return render_template('create_quote.html', title='New Quote', form=form)

        elif request.method == 'GET':
            form.delivery_address.data = current_user.user_profile.address_one + ' ' + current_user.user_profile.address_two  # current_user.user_profile.address_one
            return render_template('create_quote.html', title='New Quote', form=form)


@quotes.route("/quote/<int:quote_id>")
@login_required
def quote(quote_id):
    quote = Quote.query.get_or_404(quote_id)
    return render_template('quote.html', title=quote.id, quote=quote)
