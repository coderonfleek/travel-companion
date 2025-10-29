# 🌍 Travel Companion - AI-Powered Travel Suggestions

An intelligent travel companion app powered by Google's Gemini API that helps you discover amazing travel destinations based on your preferences.

## ✨ Features

- **Location-based Suggestions**: Get travel recommendations based on any location
- **Image-based Discovery**: Upload a landmark photo and find similar destinations
- **Personalized Preferences**: Select up to 3 travel preferences to customize suggestions
- **Weather Information**: Check current weather conditions using AI function calling
- **Beautiful UI**: Clean, responsive interface built with Bootstrap

## 🏗️ Project Structure

```
travel-companion/
├── backend/
│   ├── main.py                 # FastAPI backend application
│   ├── requirements.txt        # Python dependencies
│   └── .env                    # Environment variables (create this)
├── frontend/
│   ├── index.html             # Main HTML file
│   ├── styles.css             # Custom CSS styles
│   └── app.js                 # JavaScript logic
└── README.md                  # Project documentation
```

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/))
- Modern web browser

### Backend Setup

1. **Navigate to the backend folder**:

   ```bash
   cd backend
   ```
2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Create a `.env` file** in the backend folder:

   ```bash
   # Create the file
   touch .env  # On macOS/Linux
   type nul > .env  # On Windows
   ```
5. **Add your Gemini API key** to the `.env` file:

   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
6. **Run the backend server**:

   ```bash
   python main.py
   ```

   The backend will start on `http://localhost:8000`

### Frontend Setup

1. **Navigate to the frontend folder**:

   ```bash
   cd frontend
   ```
2. **Open `index.html` in your browser**:

   - Simply double-click the `index.html` file, OR
   - Use a local server (recommended):
     ```bash
     # Python 3
     python -m http.server 3000

     # Then open http://localhost:3000 in your browser
     ```

## 📖 How to Use

### Search by Location

1. Click on the **"Search by Location"** tab
2. Enter a city or location (e.g., "Paris", "Tokyo", "New York")
3. Select up to 3 travel preferences (optional)
4. Click **"Get Suggestions"**
5. Browse the generated travel destinations
6. Click **"Check Weather"** on any destination to see current conditions

### Search by Image

1. Click on the **"Search by Image"** tab
2. Upload an image of a landmark or place you love
3. Select up to 3 travel preferences (optional)
4. Click **"Find Similar Destinations"**
5. View destinations with similar features to your uploaded image

## 🛠️ Technologies Used

### Backend

- **FastAPI**: Modern Python web framework
- **Google Gemini AI**: Large language model API
- **Python Dotenv**: Environment variable management
- **Pillow**: Image processing
- **Pydantic**: Data validation

### Frontend

- **HTML5**: Structure
- **CSS3**: Styling
- **JavaScript (ES6+)**: Logic and API calls
- **Bootstrap 5**: UI framework
- **Bootstrap Icons**: Icon library

## 🔐 Environment Variables

Create a `.env` file in the `backend` folder:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**Important**: Never commit your `.env` file to version control. Add it to `.gitignore`.

## 📝 Notes

- The weather function is currently simulated. For production, integrate a real weather API like OpenWeatherMap.
- API responses are parsed as JSON. Ensure Gemini returns properly formatted JSON.
- The frontend uses `fetch` API which requires a modern browser.
- CORS is enabled for all origins in development. Restrict this in production.

## 🚧 Troubleshooting

### Backend won't start

- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that your `.env` file exists and contains a valid API key
- Verify Python version: `python --version` (should be 3.8+)

### Frontend can't connect to backend

- Ensure backend is running on port 8000
- Check the `API_BASE_URL` in `app.js` matches your backend URL
- Look for CORS errors in browser console

### Gemini API errors

- Verify your API key is valid and has sufficient quota
- Check your internet connection
- Review API usage limits at Google AI Studio

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed.

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome!

---

**Happy Traveling! ✈️🌴🗺️**
