import { TypeAnimation } from 'react-type-animation';

export default function Header() {
  return (
    <div className="flex flex-col items-center justify-center max-md:flex-col max-md:justify-center max-md:items-center mt-[5%]">
      <div className="text-7xl font-mono text-blue-400 m-auto mt-10 md:mt-5 max-sm:text-4xl max">
        <TypeAnimation
          sequence={[
            '% Daniel Park', 10000
          ]}
          wrapper="span"
          speed={10}
          repeat={Infinity}
        />
      </div>
      <div className="flex font-mono text-blue-400 justify-center items-center gap-x-5 mt-[2%] max-sm:flex-col max-sm:gap-x-0">
        <button class="text-2xl m-6 group relative w-max max-sm:m-2">
        <span class="relative z-10 group-hover:text-white">Biography</span>
        <span class="absolute left-0 bottom-0 w-full h-0.5 transition-all  group-hover:h-full group-hover:bg-blue-400 "></span>
        </button>
        <button class="text-2xl m-6 group relative w-max max-sm:m-2">
        <span class="relative z-10 group-hover:text-white">Projects</span>
        <span class="absolute left-0 bottom-0 w-full h-0.5 transition-all  group-hover:h-full group-hover:bg-blue-400"></span>
        </button>
        <button class="text-2xl m-6 group relative w-max max-sm:m-2">
        <span class="relative z-10 group-hover:text-white">Contact</span>
        <span class="absolute left-0 bottom-0 w-full h-0.5 transition-all  group-hover:h-full group-hover:bg-blue-400 "></span>
        </button>
      </div>
    </div>
  );
};

