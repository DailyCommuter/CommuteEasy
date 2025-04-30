// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAdWGEOthTkA9nUnvD1OkN-7wIhNmmjFos",
  authDomain: "dailycommuter-c5de3.firebaseapp.com",
  projectId: "dailycommuter-c5de3",
  storageBucket: "dailycommuter-c5de3.firebasestorage.app",
  messagingSenderId: "993390757681",
  appId: "1:993390757681:web:392d2981b47862866d1210",
  measurementId: "G-4EC63CEE21"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
