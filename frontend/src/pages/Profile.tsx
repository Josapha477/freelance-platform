import { useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { freelance_profiles } from "../services";



interface Freelance {
    id: number;
    avatar: string;
    last_name: string;
    first_name: string;
    bio: string;
    available_hour_per_week: number;
    hourly_rate: number;
    year_experience: number;
    country: string;
    skills?: { name: string; content: string };
}

const Profile = () => {
    const { id } = useParams();
    const pid = id ? Number(id) : undefined;
    const profile = pid ? (freelance_profiles as Freelance[]).find((p) => p.id === pid) : undefined;

    useEffect(() => {
        document.title = profile ? `${profile.first_name} ${profile.last_name} — Profile` : "Profiles";
    }, [profile]);

    // Single profile view
    if (profile) {
        return (
            <div className="min-h-screen">
                                                                                                                                                      
                <section className="relative h-[380px] bg-cover bg-center cover"
                    style={{
                        background: "url(/RESOURCES/cover_overlay.png) no-repeat center/100% 100%, url(/RESOURCES/cover.jpg) no-repeat center/cover"
                    }}>


                    <div className="absolute inset-0 bg-black/50"></div>

  
                    <div className="absolute top-6 left-6 border-l-4 border-orange-400 pl-3 text-sm text-white space-y-2 z-10">
                        <p><a href="mailto:mon_email@gmail.com">mon_email@gmail.com</a></p>
                        <p><a href="tel:+33612345678">06 12 34 56 78</a></p>
                    </div>

  
                    <div className="relative z-10 flex flex-col items-center justify-center h-full text-center">
                        <img src={`/RESOURCES/profile.png`}
                            className="w-24 h-24 rounded-full border-4 border-white mb-4"
                            alt="Profile" />

                        <h1 className="text-white text-4xl font-bold">Jonathan Roux</h1>
                        <p className="text-gray-300 mt-2">
                            Développeur Freelance • 16 ans d'expérience
                        </p>

                        <a href="mailto:mon_email@gmail.com"
                            className="mt-5 inline-block border-2 border-orange-400 px-6 py-2
        text-orange-400 hover:bg-orange-400 hover:text-white transition">
                            Me contacter
                        </a>
                    </div>
                </section>


                <section className="bg-gray-100 py-16 px-6 text-center">
                    <div className="w-36 h-[1px] bg-gray-400 mx-auto mb-6"></div>

                    <p className="text-xl max-w-xl mx-auto text-gray-600">
                        Je développe <strong>vos projets web</strong> et
                        <strong>applications mobiles</strong> de A à Z.
                    </p>
                </section>


                <section className="py-16 px-6 max-w-6xl mx-auto">
                    <h2 className="text-3xl font-bold text-center mb-10">En savoir plus</h2>

                    <div className="grid md:grid-cols-2 gap-10 items-center">
                        <img src="/RESOURCES/profile2.jpg"
                            className="rounded-lg shadow-lg"
                            alt="Profil secondaire" />

                        <div className="border-l-4 border-orange-400 pl-6">
                            <p className="mb-4">
                                Passionné par la programmation depuis le plus jeune âge,
                                je suis développeur professionnel avec plus de
                                <strong>16 ans d’expérience</strong>.
                            </p>

                            <p className="mb-4">
                                Expert en <strong>web</strong> et
                                <strong>applications mobiles</strong>,
                                je propose des services freelance personnalisés.
                            </p>

                            <a href="https://www.linkedin.com"
                                className="text-orange-500 font-semibold hover:underline"
                                target="_blank">
                                Voir mon profil LinkedIn →
                            </a>
                        </div>
                    </div>
                </section>


                <section className="bg-gray-100 py-20 px-6">
                    <h2 className="text-3xl font-bold text-center mb-14">Portfolio</h2>

                    <div className="grid md:grid-cols-2 gap-12 max-w-6xl mx-auto">

   
                        <div className="flex gap-4 items-start">
                            <div className="w-1 bg-orange-400"></div>
                            <div>
                                <a href="#">
                                    <img src="project1small.jpg"
                                        className="rounded-lg shadow hover:scale-105 transition"
                                        alt="" />
                                </a>
                                <p className="mt-3 text-center font-medium">
                                    Site web pour un restaurant
                                </p>
                            </div>
                        </div>

    
                        <div className="flex gap-4 items-start">
                            <div className="w-1 bg-orange-400"></div>
                            <div>
                                <a href="#">
                                    <img src="project2small.jpg"
                                        className="rounded-lg shadow hover:scale-105 transition"
                                        alt="" />
                                </a>
                                <p className="mt-3 text-center font-medium">
                                    Application mobile IA
                                </p>
                            </div>
                        </div>

                    </div>
                </section>


                {/* <section className="py-16 px-6 max-w-4xl mx-auto">
                    <iframe src="contact-frame.html"
                        className="w-full h-[350px] border-none rounded-lg shadow">
                    </iframe>
                </section> */}
            </div>
        )
    }  
};

                    

export default Profile