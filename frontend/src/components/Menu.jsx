const Menu= () =>{
    return(
        <>
            <div className="menu">
                <div className="item">
                    <span className="tile p-4 text-sm"> Main </span>
                    <a href="/" className="list flex items-center gap-1.5 p-4 hover:bg-blue-100">
                        <img className="w-8 h-8 object-cover object-center" src="./home.png"></img>
                        <span>HOME</span>
                    </a>
                    <a href="/" className="list flex items-center gap-1.5 p-3 hover:bg-blue-100">
                        <img className="w-8 h-8 object-cover object-center" src="./user.png"></img>
                        <span>PROFILE</span>
                    </a> 
                </div>
                <div className="item">
                    <span className="tile p-4 text-sm"> Analytics </span>
                    <a href="/" className="list flex items-center gap-1.5 p-4 hover:bg-blue-100">
                        <img className="w-8 h-8 object-cover object-center" src="./bar-chart.png"></img>
                        <span>BAR GRAPH</span>
                    </a>
                    <a href="/" className="list flex items-center gap-1.5 p-3 hover:bg-blue-100">
                        <img className="w-8 h-8 object-cover object-center" src="./pie-chart.png"></img>
                        <span>PIE CHART</span>
                    </a> 
                </div>
                
            </div>
        </>
    )
}

export default Menu;