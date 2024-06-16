import logo from './freshfeed.png';
import reload_button from './Reload button freshfeed.png'
import React from 'react';
import "./Header.css" 


const Header = () =>  {
  return (
      <>
      <img className = "logo" src={logo} alt="Logo" />
      <div className="vl">
      
      <a href='/'>
      <img className = "reload" src={reload_button} alt="Logo" />
      </a>
      </div>
      </>
  );
}

export default Header;