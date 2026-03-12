import { freelance_profiles, welcom_text } from "../services"
import { ProfileCard } from "./cards/ProfileCard"

export default function Section() {
    return (
		<div className="pt-32 pb-24 bg-gray-50">
			<div className="max-w-7xl mx-auto px-6 
			md:grid-cols-2 gap-12 items-center">
				<div className="">
					<h1 className="text-5xl font-bold
					 leading-tight mb-6 gap-2 lg:text-3xl">
						{welcom_text.text1}
						 <span className="text-blue-600">
							 plus vite	
						 </span>
					</h1>
				</div>
				<p className="text-xl text-gray-600 mb-8">
					{welcom_text.text2}
				</p>
				<div className="flex space-x-4 justify-center">
					<button className="bg-blue-600
					 text-white px-8 py-3 rounded-lg text-lg hover:bg-blue-700">
						Demarrer
					</button>
					<button className="border border-gray-300 text-black
					  px-8 py-3 rounded-lg text-lg hover:bg-gray-100">
						Voir Demo
					</button>
				</div>

				<section className="py-24">
					<h2 className="text-4xl font-bold mb-4">Nos meilleurs Freelance</h2>
				<div className="grid md:grid-cols-3 gap-10">
			{freelance_profiles.map((p) => (
					<ProfileCard freelance={p} key={p.id}/>
				))}
						
			</div>
			</section>
			</div>
	</div>
		
    )
}