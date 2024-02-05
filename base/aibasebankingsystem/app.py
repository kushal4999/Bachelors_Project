from base import app

port_number = 7576

if __name__ == "__main__":
    app.run(threaded=True, host='localhost', port=port_number, debug=True)
