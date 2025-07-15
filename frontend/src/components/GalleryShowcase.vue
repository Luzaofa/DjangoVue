<template>
    <div class="gallery-container">
        <div class="gallery-card">

            <div v-if="loading">正在加载艺术作品...</div>
            <div v-else-if="error">{{ error }}</div>

            <div v-else>
                <transition name="fade" mode="out-in">
                    <img
                            :src="currentArtwork.image"
                            :key="currentArtwork.image"
                            class="artwork-image"
                            alt="art"
                    />
                </transition>

                <div class="artwork-details">
                    <h2 class="artwork-title">{{ currentArtwork.title }}</h2>
                    <p class="artwork-meta">
                        {{ currentArtwork.artist }} · {{ currentArtwork.year }}
                    </p>
                    <p class="artwork-desc">{{ currentArtwork.description }}</p>
                    <p class="artwork-stats">
                        ❤️ {{ currentArtwork.likes }}　👁️ {{ currentArtwork.views }}
                    </p>
                </div>

                <div class="nav-buttons">
                    <button @click="prevSlide">←</button>
                    <span>{{ currentIndex + 1 }} / {{ artworks.length }}</span>
                    <button @click="nextSlide">→</button>
                </div>

                <div class="thumbnail-bar">
                    <img
                            v-for="(art, index) in artworks"
                            :key="art.id"
                            :src="art.image"
                            :class="{ active: index === currentIndex }"
                            class="thumbnail"
                            @click="goToSlide(index)"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import {ref, computed, onMounted, onUnmounted} from 'vue'
import axios from 'axios'

const artworks = ref([])
const currentIndex = ref(0)
const interval = ref(null)
const loading = ref(true)
const error = ref(null)

const fetchArtworks = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/datas/')
        artworks.value = response.data
        loading.value = false
    } catch (err) {
        error.value = '加载艺术作品失败，请稍后重试。'
        loading.value = false
    }
}

const nextSlide = () => {
    if (artworks.value.length === 0) return
    currentIndex.value = (currentIndex.value + 1) % artworks.value.length
}

const prevSlide = () => {
    if (artworks.value.length === 0) return
    currentIndex.value = (currentIndex.value - 1 + artworks.value.length) % artworks.value.length
}

const goToSlide = (index) => {
    currentIndex.value = index
}

const currentArtwork = computed(() => artworks.value[currentIndex.value] || {})

onMounted(() => {
    fetchArtworks()
    interval.value = setInterval(() => {
        nextSlide()
    }, 5000)
})

onUnmounted(() => {
    clearInterval(interval.value)
})
</script>


<style scoped>
.gallery-container {
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #1e1e2f, #2d2d44);
    min-height: 100vh;
}

.gallery-card {
    max-width: 800px;
    background: #ffffff10;
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(12px);
    color: #fff;
    text-align: center;
    transition: all 0.3s ease;
}

.artwork-image {
    width: 100%;
    height: auto;
    border-radius: 16px;
    margin-bottom: 1rem;
    object-fit: cover;
    max-height: 450px;
    transition: transform 0.5s ease;
}

.artwork-image:hover {
    transform: scale(1.02);
}

.artwork-title {
    font-size: 2rem;
    margin: 0.5rem 0;
}

.artwork-meta {
    font-size: 1rem;
    opacity: 0.7;
}

.artwork-desc {
    margin-top: 0.8rem;
    font-size: 1.1rem;
    line-height: 1.6;
}

.artwork-stats {
    margin-top: 0.6rem;
    font-size: 1rem;
}

.nav-buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 1.5rem 0;
}

.nav-buttons button {
    padding: 0.5rem 1rem;
    border: none;
    background: #ffffff33;
    color: white;
    font-size: 1.2rem;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.3s ease;
}

.nav-buttons button:hover {
    background: #ffffff55;
}

.thumbnail-bar {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-top: 1rem;
    flex-wrap: wrap;
}

.thumbnail {
    width: 60px;
    height: 45px;
    object-fit: cover;
    border: 2px solid transparent;
    border-radius: 6px;
    cursor: pointer;
    transition: transform 0.3s ease, border 0.3s ease;
}

.thumbnail:hover {
    transform: scale(1.1);
}

.thumbnail.active {
    border: 2px solid #fff;
}

.fade-enter-active, .fade-leave-active {
    transition: opacity 0.6s;
}

.fade-enter-from, .fade-leave-to {
    opacity: 0;
}

</style>
