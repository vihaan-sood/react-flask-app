import logo from './freshfeed.png';
import reload_button from './Reload button freshfeed.png'
import React from 'react';


const Header = () =>  {
  return (
      <>
      <img src={logo} alt="Logo" />
      <a href='/'>
      <img src={reload_button} alt="Logo" />
      </a>
      </>
  );
}

export default Header;