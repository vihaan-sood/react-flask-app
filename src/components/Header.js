import logo from './freshfeed.png';
import reload_button from './Reload button freshfeed.png'
import React from 'react';
import "./Layout.css" 


// const Header = () =>  {
//   return (
//       <>
//       <img className = "logo" src={logo} alt="Logo" />
//       <div className="vl">
      
//       <a href='/'>
//       <img className = "reload" src={reload_button} alt="Logo" />
//       </a>
//       </div>
//       </>
//   );
// }


const Header = () => {
  return (
    <header className="header">
      <div className="header-section">
      <img className = "logo" src={logo} alt="Logo" />

      </div>
      <div className="header-section">
      <a href='/'>
      <img className = "reload" src={reload_button} alt="Logo" />
      </a>
        <p>Reload Page</p>
      </div>
    </header>
  );
};

export default Header;


