import matplotlib.pyplot as plt
import seaborn as sns

def apply_chart_style(fig, ax, title, xlabel="", ylabel=""):
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#161b22')
    
    # Graphs Titles: Forced to Red-Pink-Orange mix color scheme
    ax.set_title(title, fontsize=12, fontweight='bold', pad=30, color='#ff007f', 
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
    
    # FIX: Using suptitle with perfect Y-positioning so it never overlaps the box title
    fig.suptitle("🔴 Red = Deceased  |  💗 Pink = Survived", 
                 color='#ffffff', fontsize=10, weight='bold', y=0.85)
    
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
        surv_col = 'survived' if 'survived' in df.columns else ('Survived' if 'Survived' in df.columns else None)
        age_col = 'age' if 'age' in df.columns else ('Age' if 'Age' in df.columns else 'age')
        fare_col = 'fare' if 'fare' in df.columns else ('Fare' if 'Fare' in df.columns else 'fare')
        
        sns.scatterplot(data=df, x=age_col, y=fare_col, hue=surv_col, ax=ax, palette=['#ffb703', '#1f77b4'], alpha=0.9, s=55, edgecolor='#ffffff')
        legend = ax.legend(title='Status', facecolor='#0e1117', edgecolor='none')
        plt.setp(legend.get_texts(), color='#8b949e')
    
    # FIX: Subtitle added safely below the boxed title header
    fig.suptitle("🟡 Yellow = Deceased (0)  |  🔵 Blue = Survived (1)", 
                 color='#ffffff', fontsize=10, weight='bold', y=0.85)
                 
    apply_chart_style(fig, ax, 'Passenger Fare vs Age', 'Age', 'Fare')
    return fig

def draw_gender_survival(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.countplot(data=df, x='sex', hue='survived', ax=ax, palette=['#00f5d4', '#ffb703'], edgecolor='#ffffff', linewidth=0.8)
        legend = ax.legend(labels=['Deceased', 'Survived'], facecolor='#0e1117', edgecolor='none')
        plt.setp(legend.get_texts(), color='#8b949e')
        
    # FIX: Subtitle alignment fix
    fig.suptitle("🟢 Teal = Deceased (0)  |  🟡 Yellow = Survived (1)", 
                 color='#ffffff', fontsize=10, weight='bold', y=0.85)
                 
    apply_chart_style(fig, ax, 'Survival Count by Gender', 'Gender', 'Count')
    return fig

def draw_embark_count(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    emb_col = 'embarked' if 'embarked' in df.columns else ('embark_town' if 'embark_town' in df.columns else None)
    if not df.empty and emb_col:
        sns.countplot(data=df, x=emb_col, ax=ax, palette=['#ff3333', '#ff007f', '#ff758f'], edgecolor='#ffffff')
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
        
    # FIX: Subtitle alignment fix
    fig.suptitle("💗 Pink = Deceased (0)  |  🟡 Yellow = Survived (1)", 
                 color='#ffffff', fontsize=10, weight='bold', y=0.85)
                 
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
    fig, ax = plt.subplots(figsize=(6, 4))
    age_col = 'Age' if 'Age' in df.columns else 'age'
    fare_col = 'Fare' if 'Fare' in df.columns else 'fare'
    pclass_col = 'Pclass' if 'Pclass' in df.columns else 'pclass'
    surv_col = 'Survived' if 'Survived' in df.columns else 'survived'
    
    if not df.empty:
        scatter = ax.scatter(
            x=df[age_col], 
            y=df[fare_col], 
            s=df[pclass_col] * 50,  
            c=df[surv_col],     
            cmap='coolwarm', 
            alpha=0.6, 
            edgecolors="white"
        )
        
    # FIX: Clear coolwarm description subtitle
    fig.suptitle("💙 Blue Tone = Deceased (0)  |  ❤️ Red Tone = Survived (1)", 
                 color='#ffffff', fontsize=10, weight='bold', y=0.85)
            
    apply_chart_style(fig, ax, "Bonus Chart: Age vs Fare (Bubble Size by Pclass)", "Passenger Age", "Ticket Fare")
    return fig
