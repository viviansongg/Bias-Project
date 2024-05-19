// src/Popup.js
import React from 'react';
import './Popup.css'; // For custom styling

const Popup = ({ isOpen, onClose, children }) => {
  if (!isOpen) return null;

  return (
    <div className="popup-overlay">
      <div className="popup-box">
        <button className="popup-close" onClick={onClose}>
          &times;
        </button>
        <div className="popup-content">
          {children}
        </div>
      </div>
    </div>
  );
};

export default Popup;
