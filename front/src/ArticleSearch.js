import React from 'react';
import './ArticleSearch.css';

function ArticleSearch() {
  return (
    <div> 
      <div className="container"> 
      <input
        className= "article-screen-searchbar"
        type="text"
        placeholder="" //should be equal to user entry
      />
      <br></br>
      <div className= "scrollable-body"> 
        <div className="scroll-container">
        <div className= "article-body">
          <h2 className= "article-name">articleName</h2>
          <span className= "article-description">article description</span>
        </div> 
        <div className= "article-body">
          <h2 className= "article-name">articleName</h2>
          <span className= "article-description">article description</span>
        </div> 
        <div className= "article-body">
          <h2 className= "article-name">articleName</h2>
          <span className= "article-description">article description</span>
        </div> 
        <div className= "article-body">
          <h2 className= "article-name">articleName</h2>
          <span className= "article-description">article description</span>
        </div> 
        </div>
      </div>
      </div>

  

    </div>
  );
}

export default ArticleSearch;
