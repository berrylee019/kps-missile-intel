import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time
from streamlit_autorefresh import st_autorefresh

# 1. 페이지 설정
st.set_page_config(page_title="KPS-IR Integrated Missile Intelligence", layout="wide")

# 2. 군사 작전용 스타일 적용
st.markdown("""
    <style>
    .stApp { background: #030508; color: #f0f2f6; }
    .alert-banner {
        background: rgba(255, 75, 75, 0.2);
        border: 1px solid #ff4b4b;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    .metric-panel {
        background: #0d131f;
        border: 1px solid #1a2a40;
        padding: 15px;
        border-radius: 6px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 자동 새로고침 (실시간 감시 시뮬레이션 - 10초 주기)
st_autorefresh(interval=10000, key="kps_integrated_sync")

# 4. 세션 스테이트 초기화 (과거 데이터 + 실시간 누적 관리)
if 'missile_logs' not in st.session_state:
    st.session_state.missile_logs = [
        {
            "id": "LOG-2026-0812",
            "date": "2026-08-12 06:00",
            "origin": "원산 일대",
            "lat": 39.15, "lon": 127.45,
            "target_lat": 39.0, "target_lon": 134.5,
            "distance": "700km 이상",
            "type": "SRBM (1발 단독)",
            "status": "ARCHIVED",
            "color": "#ffaa00"
        },
        {
            "id": "LOG-2026-0820",
            "date": "2026-08-20 17:00",
            "origin": "평양 일대",
            "lat": 39.03, "lon": 125.75,
            "target_lat": 39.2, "target_lon": 129.5,
            "distance": "300km 내외",
            "type": "600mm 초대형 방사포 (10여 발)",
            "status": "RECENT ACTIVE",
            "color": "#ff4b4b"
        }
    ]

# 실시간 감시 센서 모사 (확률적으로 새로운 가상 도발 데이터 추가)
np.random.seed(int(time.time() // 30))
if np.random.rand() < 0.15: # 15% 확률로 신규 탐지 이벤트 시뮬레이션
    new_id = f"LIVE-{datetime.now().strftime('%H%M%S')}"
    if not any(l['id'] == new_id for l in st.session_state.missile_logs):
        st.session_state.missile_logs.append({
            "id": new_id,
            "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "origin": "황해북도 일대",
            "lat": 38.5, "lon": 126.0,
            "target_lat": 38.8, "target_lon": 128.5,
            "distance": "350km",
            "type": "실시간 탐지 미상 발사체",
            "status": "CRITICAL LIVE",
            "color": "#00d4ff"
        })

# --- UI 레이아웃 ---
st.title("🛰️ KPS-INTEL : 한반도 미사일 정찰 및 역사적 도발 통합 대시보드")
st.markdown(f"**Sources:** `USSF SBIRS` + `합동참모본부 아카이브` | **Status:** <span style='color:#00ff41;'>● LIVE MONITORING ACTIVE</span> | **Sync Time:** `{datetime.now().strftime('%H:%M:%S')}`", unsafe_allow_html=True)

st.divider()

# 최신 경고 배너
st.markdown("""
<div class='alert-banner'>
    <h3 style='color: #ff4b4b; margin:0;'>🚨 2026년 8월 20일 금일 작전 상황: 평양 일대 SRBM 10여 발 무더기 발사 감지 완료</h3>
    <p style='margin: 5px 0; font-size: 0.9rem;'>미 우주군 적외선 정찰위성(SBIRS) 및 국내외 센서 데이터를 기반으로 과거 도발 궤적과 실시간 궤적이 통합 시각화되고 있습니다.</p>
</div>
""", unsafe_allow_html=True)

# 상단 핵심 지표
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"<div class='metric-panel'>총 기록된 도발 횟수<br><h3>{len(st.session_state.missile_logs)} Cases</h3></div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='metric-panel'>금일(8.20) 발사 규모<br><h3 style='color:#ff4b4b;'>10+ Units (방사포)</h3></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='metric-panel'>위성 센서 응답 속도<br><h3 style='color:#00ff41;'>0.38 sec</h3></div>", unsafe_allow_html=True)
with c4:
    st.markdown("<div class='metric-panel'>한미일 정보 공유<br><h3 style='color:#00d4ff;'>SYNCED (100%)</h3></div>", unsafe_allow_html=True)

st.write("")

# 메인 레이아웃: 좌측은 도발 리스트 로그, 우측은 통합 지도 시각화
col_left, col_right = st.columns([1, 2])

with col_left:
    st.subheader("📋 통합 도발 이력 및 실시간 로그")
    for log in reversed(st.session_state.missile_logs):
        st.markdown(f"""
        <div style='background: #0a101d; border: 1px solid {log["color"]}; padding: 10px; border-radius: 6px; margin-bottom: 8px;'>
            <small style='color: {log["color"]}; font-weight:bold;'>[{log['status']}] {log['id']}</small><br>
            <b>일시:</b> {log['date']}<br>
            <b>발사 원점:</b> {log['origin']}<br>
            <b>무기 체계:</b> {log['type']}<br>
            <b>비행 거리:</b> {log['distance']}
        </div>
        """, unsafe_allow_html=True)

with col_right:
    st.subheader("🗺️ 역사적 도발 및 실시간 궤적 통합 관제 맵")
    
    fig = go.Figure()
    
    # 모든 로그를 순회하며 지도에 트레이스 추가
    for log in st.session_state.missile_logs:
        fig.add_trace(go.Scattergeo(
            lat=[log['lat'], log['target_lat']],
            lon=[log['lon'], log['target_lon']],
            mode='lines+markers',
            name=f"{log['id']} ({log['type']})",
            line=dict(color=log['color'], width=3 if log['status'] != 'ARCHIVED' else 2),
            marker=dict(size=7, color=log['color'])
        ))
        
    fig.update_geos(
        scope='asia',
        center=dict(lat=39.0, lon=127.0),
        projection_scale=6,
        bgcolor="#030508",
        showland=True, landcolor="#0a101d",
        showocean=True, oceancolor="#030508",
        showcountries=True, countrycolor="#1a2a40"
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0), 
        paper_bgcolor='rgba(0,0,0,0)', 
        legend=dict(x=0.01, y=0.99, font=dict(size=10, color='white'))
    )
    
    st.plotly_chart(fig, use_container_width=True)
