from flask import Flask, render_template

app = Flask(__name__)

BIDDER_OPTION = {
    'bidder_location': ['Delhi', 'Tamil Nadu', 'Rajasthan', 'Kerala', 'Andhra Pradesh', 'Bihar', 'Punjab', 'Telangana', 'Gujarat', 'Madhya Pradesh'],
  
    'tender_type_name': ['Open Tender', 'Limited', 'Open Limited', 'Global Tenders', 'EOI', 'Test'],
  
    'tender_category_name': ['Works', 'Goods', 'Services'],
  
    'tender_form_contract_name': ['Item Rate', 'Percentage', 'Item Wise', 'Supply', 'Lump-sum','Supply and Service', 'Service', 'Fixed-rate', 'Tender cum Auction', 'Turn-key', 'Piece-work']
  }

@app.route("/")
def hello_world():
  return render_template('home.html', bidder_option = BIDDER_OPTION)



if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)