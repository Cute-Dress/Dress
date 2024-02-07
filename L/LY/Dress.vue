<!--vite ^4.2.0, vuetify ^3.0.0, see https://github.com/Young-Lord/online-clipboard/blob/v0.0.4/frontend/package.json-->
<template>
    <v-app>
        <v-main>
            <v-container fluid class="fill-height justify-center">
                <v-col cols="12" md="8">
                    <v-card elevation="16" variant="tonal">
                        <v-card-title>
                            <span class="headline">Welcome to Dress!</span>
                        </v-card-title>
                        <v-card-text>
                            <v-form @submit.native.prevent>
                                <v-text-field v-model="name" label="Who?" required
                                    @keydown.enter="goToDress"></v-text-field>
                                <v-btn color="primary" @click="goToDress" :disabled="!name" block>
                                    Go!
                                </v-btn>
                            </v-form>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
export default {
    data() {
        return {
            name: "LY",
        }
    },
    created() { },
    methods: {
        goToDress() {
            window.location.href = `https://github.com/Cute-Dress/Dress/tree/master/${this.name}`
        }
    },
}
</script>
