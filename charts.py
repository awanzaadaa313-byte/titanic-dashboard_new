import matplotlib.pyplot as plt
import seaborn as sns

def apply_chart_style(fig, ax, title, xlabel="", ylabel=""):
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#161b22')
    
    # Graphs Titles: Forced to Red-Pink-Orange mix color scheme
    ax.set_title(title, fontsize=14, fontweight='bold', pad=15, color='#ff007f', 
                 bbox=dict(facecolor='none', edgecolor='#ff4500', pad=4, linewidth=1)) 
    
    if xlabel: ax.set_xlabel(xlabel, fontsize=10, color='#ff3333', labelpad=8, fontweight='bold')
    if ylabel: ax.set_ylabel(ylabel, fontsize=10, color='#ff3333', labelpad=8, fontweight='bold')
    
    ax.tick_params(colors='#ff4500', labelsize=10, width=2)
    ax.grid(True, linestyle=':', alpha=0.15, color='#ffffff')
    
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    fig.tight_layout()

def draw_bar_chart(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        colors = ['#1f77b4', '#e63946', '#ff007f'] 
        sns.barplot(data=df, x='pclass', y='fare', ax=ax, palette=colors, errorbar=None, edgecolor='#ffffff', linewidth=1)
    apply_chart_style(fig, ax, 'Class-wise Average Fare', 'Ticket Class', 'Average Fare')
    return fig

def draw_pie_chart(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty and 'survived' in df.columns:
        counts = df['survived'].value_counts()
        colors = ['#ff3333', '#ff007f'] 
        labels = ['Deceased', 'Survived']
        ax.pie(counts, autopct='%1.1f%%', startangle=90, colors=colors, labels=labels, 
               textprops=dict(color="#ffffff", weight="bold", fontsize=10),
               wedgeprops=dict(width=0.45, edgecolor='#0e1117', linewidth=3))
    apply_chart_style(fig, ax, 'Survival Rate Status')
    return fig

def draw_age_dist(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.histplot(data=df, x='age', bins=20, kde=True, ax=ax, color='#ff007f', alpha=0.7, edgecolor='#ffb703', linewidth=1.2)
        if ax.lines:
            ax.lines[0].set_color('#ff4500')
            ax.lines[0].set_linewidth(3)
    apply_chart_style(fig, ax, 'Age Distribution of Passengers', 'Passenger Age', 'Count')
    return fig

def draw_scatter_fare_age(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.scatterplot(data=df, x='age', y='fare', hue='survived', ax=ax, palette=['#ffb703', '#1f77b4'], alpha=0.9, s=55, edgecolor='#ffffff')
        legend = ax.legend(title='Status', facecolor='#0e1117', edgecolor='none')
        plt.setp(legend.get_texts(), color='#8b949e')
    apply_chart_style(fig, ax, 'Passenger Fare vs Age', 'Age', 'Fare')
    return fig

def draw_gender_survival(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.countplot(data=df, x='sex', hue='survived', ax=ax, palette=['#00f5d4', '#ffb703'], edgecolor='#ffffff', linewidth=0.8)
        legend = ax.legend(labels=['Deceased', 'Survived'], facecolor='#0e1117', edgecolor='none')
        plt.setp(legend.get_texts(), color='#8b949e')
    apply_chart_style(fig, ax, 'Survival Count by Gender', 'Gender', 'Count')
    return fig

def draw_embark_count(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty and 'embarked' in df.columns:
        sns.countplot(data=df, x='embarked', ax=ax, palette=['#ff3333', '#ff007f', '#ff758f'], edgecolor='#ffffff')
    apply_chart_style(fig, ax, 'Passengers per Embarkation Port', 'Port of Embarkation', 'Count')
    return fig

def draw_fare_box(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.boxplot(data=df, x='pclass', y='fare', ax=ax, palette=['#00f5d4', '#ffb703', '#1f77b4'], fliersize=3)
    apply_chart_style(fig, ax, 'Fare Distribution by Class', 'Ticket Class', 'Fare')
    return fig

def draw_age_violin(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.violinplot(data=df, x='pclass', y='age', hue='survived', split=True, ax=ax, palette=['#ff007f', '#ffb703'], inner="quart")
        legend = ax.legend(facecolor='#0e1117', edgecolor='none')
        plt.setp(legend.get_texts(), color='#8b949e')
    apply_chart_style(fig, ax, 'Age Distribution by Class & Survival', 'Ticket Class', 'Age')
    return fig

def draw_sibsp_count(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.countplot(data=df, x='sibsp', ax=ax, color='#1f77b4', edgecolor='#ff3333', linewidth=1.5, alpha=0.9)
    apply_chart_style(fig, ax, 'Number of Siblings/Spouses Aboard', 'SibSp Count', 'Passenger Count')
    return fig

def draw_parch_count(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.countplot(data=df, x='parch', ax=ax, color='#ffb703', edgecolor='#1f77b4', linewidth=1.5, alpha=0.9)
    apply_chart_style(fig, ax, 'Number of Parents/Children Aboard', 'Parch Count', 'Passenger Count')
    return fig
def draw_bonus_bubble_chart(df):
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    fig, ax = plt.subplots(figsize=(6, 4))
    scatter = ax.scatter(
        x=df['Age'], 
        y=df['Fare'], 
        s=df['Pclass'] * 50,  
        c=df['Survived'],     
        cmap='coolwarm', 
        alpha=0.6, 
        edgecolors="white"
    )
    ax.set_title("Bonus Chart: Age vs Fare (Bubble Size by Pclass)", fontsize=12, fontweight='bold', color='#1e3d59')
    ax.set_xlabel("Passenger Age", fontsize=10)
    ax.set_ylabel("Ticket Fare", fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.5)
    
    return fig
    # --- Interactive Data Explorer Pane ---
st.markdown("<span class='section-title'>🔍 Live Passenger Data Explorer</span>", unsafe_allow_html=True)
st.markdown("<div class='heading-line-1'></div><div class='heading-line-2'></div>", unsafe_allow_html=True)

# Search Input
search_query = st.text_input("Search Passenger by Name (Real-time Filter):", "").strip()

# Apply search filter if text is entered
if search_query:
    display_df = filtered_df[filtered_df['name'].str.contains(search_query, case=False, na=False)]
else:
    display_df = filtered_df

# Display dataframe with premium styling
st.dataframe(display_df.head(100), use_container_width=True)
st.caption(f"Showing {len(display_df)} rows based on current active filters and search query.")
