import Section from "../components/Section";
import Footer from "../components/Footer";
import { useEffect } from "react";


const Home = () => {

	useEffect(() => {
		document.title = "Home"
	}, [])

	return (
		<div className="text-gray-800 text-extrabold">
				<Section></Section>
				<Footer></Footer>
		</div>
)

}

export default Home
