from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Dummy database to store notes
notes = []

# Dummy API key for UIUC Course Explorer API
UIUC_API_KEY = os.environ.get('UIUC_API_KEY')

# Route to upload notes
@app.route('/upload-note', methods=['POST'])
def upload_note():
    # Here you would implement logic to handle file upload
    # For simplicity, let's assume the uploaded note is saved to some storage and relevant data is stored in the 'notes' list
    data = request.get_json()
    notes.append(data)
    return jsonify({'message': 'Note uploaded successfully'})

# Route to edit note
@app.route('/edit-note/<int:note_id>', methods=['PUT'])
def edit_note(note_id):
    # Here you would implement logic to edit a note based on its ID
    # For simplicity, let's just update the note's content in the 'notes' list
    data = request.get_json()
    notes[note_id] = data
    return jsonify({'message': 'Note edited successfully'})

# Route to delete note
@app.route('/delete-note/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    # Here you would implement logic to delete a note based on its ID
    # For simplicity, let's just remove the note from the 'notes' list
    del notes[note_id]
    return jsonify({'message': 'Note deleted successfully'})

# Route to get all notes
@app.route('/notes', methods=['GET'])
def get_all_notes():
    return jsonify(notes)

# Route to get list of all UIUC classes
@app.route('/uiuc-classes', methods=['GET'])
def get_uiuc_classes():
    # Here you would implement logic to fetch data from UIUC Course Explorer API
    # For simplicity, let's assume we have access to the API and fetch data using the API key
    # UIUC_API_KEY = 'YOUR_UIUC_API_KEY'
    # You would replace this with your actual API call
    uiuc_classes = [{'course_code': 'CS101', 'course_name': 'Introduction to Computer Science'},
                    {'course_code': 'ENG101', 'course_name': 'English Composition'}]  # Example data
    return jsonify(uiuc_classes)

if __name__ == '__main__':
    app.run(debug=True) 