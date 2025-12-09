module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],

    darkMode: 'class',

    theme: {
        container: {
            center: true,
            padding: "2rem",
            screens: {
                "2xl": "1400px",
            },
        },

        extend: {
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
            },

            colors: {
                border: "hsl(214 18% 89%)",
                input: "hsl(214 18% 89%)",
                ring: "hsl(219 87% 25%)",
                background: "hsl(220 40% 98%)",
                foreground: "hsl(220 15% 20%)",

                primary: {
                    DEFAULT: "hsl(219 87% 25%)",
                    foreground: "hsl(0 0% 100%)",
                    light: "hsl(217 76% 48%)",
                },

                secondary: {
                    DEFAULT: "hsl(210 40% 96%)",
                    foreground: "hsl(219 87% 25%)",
                },

                muted: {
                    DEFAULT: "hsl(210 20% 96%)",
                    foreground: "hsl(213 9% 39%)",
                },

                accent: {
                    DEFAULT: "hsl(217 76% 48%)",
                    foreground: "hsl(0 0% 100%)",
                },

                card: {
                    DEFAULT: "hsl(0 0% 100%)",
                    foreground: "hsl(213 15% 16%)",
                },

                success: {
                    DEFAULT: "hsl(155 60% 45%)",
                    foreground: "hsl(0 0% 100%)"
                }
            },

            backgroundImage: {
                'gradient-hero':
                    'linear-gradient(135deg, hsl(219 87% 25%), hsl(217 76% 48%))',
            },

            boxShadow: {
                'soft':
                    '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)',
                'medium':
                    '0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)',
                'large':
                    '0 25px 50px -12px rgb(0 0 0 / 0.25)',
            },

            // Matches your inline utilities
            backgroundColor: {
                background: "hsl(220 40% 98%)",
                card: "hsl(0 0% 100%)",
            }
        },
    },

    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
